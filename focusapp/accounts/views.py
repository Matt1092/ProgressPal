# Defines logic for handling user authentication actions in accounts app
# Includes views for registering a new user, logging in, logging out, and rendering the home page
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Imports for RESTful API implementation
from rest_framework import viewsets
from .serializers import UserSerializer


# Added class for RESTful APIs
class UserViewSet(viewsets.ModelViewSet):
    # Defines the queryset to be used for retrieving user data
    queryset = User.objects.all()

    # Specifies the serializer class to be used for serializing and deserializing user data
    serializer_class = UserSerializer


# Home view
# View that renders homepage for the app
def home(request):
    # Renders the main.html template
    # Pass variable year to display the year
    return render(request, 'accounts/main.html', {'year': 2024})  # Update the year dynamically as needed


# Logout view
# View that handles user logout functionality
@login_required  # Decorator ensuring that view is only accessible to logged-in users
                 # If non-logged in user tries to access it, they will be redirected to login page
def user_logout(request):
    logout(request)           # Logs the user out of the session
    return redirect('login')  # After logging out, user is redirected to login page


# Login view
# View that handles user login
def user_login(request):    # Argument request contains all the data sent from the client (form data)
    # Checks if request method is POST (form has been submitted)
    if request.method == 'POST':
        # Process the data
        # Otherwise, render the form for the user to fill out
        # Creates an instance of the AuthenticationForm using data sent with the POST request
        # AuthenticationForm is a built-in Django form that validates the user's credentials
        form = AuthenticationForm(data=request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # Extract username and data from the cleaned data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # This authenticate function checks if the provided username and password match an existing user in the database
            # If correct, returns corresponding user object and otherwise, returns None
            user = authenticate(username=username, password=password)
            # Checks if the authenticate function returned a valid user object
            if user is not None:
                # If authenticated successfully, login function logs user in by creating a session for them
                # User's ID is saved in the session, and they are now logged in
                login(request, user)
                return redirect('task_list')    # After logging in user, they are redirected to the task_list view from tasks app
    # If request method isn't POST (form not submitted yet), a new and empty AuthenticationForm is created
    # Rendered for the user to fill out
    else:
        form = AuthenticationForm()
    # Whether it's POST or GET request (when form is empty), render the login.html template passing the form instance as context
    # This allows the form to be displayed in the template
    return render(request, 'accounts/login.html', {'form': form})


# Registration view
# View that handles user registration
def register(request):      # Argument request contains all the data sent from the client (form data)
    # Checks if request method is POST (form has been submitted)
    if request.method == 'POST':
        # Process the data
        # Otherwise, display the registration form for the user to fill out
        # Creates an instance of the UserCreationForm with the data sent from the client (request.POST)
        # UserCreationForm is a built-in Django form for creating a new user, and it validates the username and password
        form = UserCreationForm(request.POST)
        # Checks if the form data is valid
        # UserCreationForm will automatically check if the username is unique and if the password matches the confirmation field
        if form.is_valid():
            # If form is valid, save the new user to the database
            # The save() method creates a new User object and stores it in the database
            user = form.save()
            # After saving new user, the login function is called, which logs the user in by creating a session
            # The user is immediately authenticated after registration, and the request.user will refer to newly registered user
            login(request, user)
            return redirect('task_list')  # After logging in user, they are redirected to the task_list view from tasks app
    # If request method isn't POST (form not submitted yet), create an empty UserCreationForm instance
    else:
        form = UserCreationForm()
    # Render register.html template, passing form instance as variable
    # If GET request, empty form is displayed for user to fill
    return render(request, 'accounts/register.html', {'form': form})
