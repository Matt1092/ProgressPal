# Defines the URL routing for the accounts app in Django
# Maps URLs to specific view functions that handle the logic for each URL
from django.urls import path                            # Path function to define URL patterns
from .views import register, user_login, user_logout    # View functions from the views.py file


# Defines a list of URL patterns for this app
urlpatterns = [
    path('register/', register, name='register'),       # Maps URL /register/ to the register view function
    path('login/', user_login, name='login'),           # Maps URL /login/ to the login view function
    path('logout/', user_logout, name='logout'),        # Maps URL /logout/ to the logout view function
]
