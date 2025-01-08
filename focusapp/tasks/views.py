# Defines logic for handling task actions in tasks app
# Includes views for viewing task progress (completed, in progress), creating a task, etc
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import json
from django.http import JsonResponse
from django.db.models import Count
from django.utils.timezone import now, timedelta
# Imports for RESTful API implementation
from rest_framework import viewsets
from .serializers import TaskSerializer


# Added class for RESTful APIs
class TaskViewSet(viewsets.ModelViewSet):
    # Defines the queryset to be used for retrieving task data
    queryset = Task.objects.all()

    # Specifies the serializer class to be used for serializing and deserializing user task data
    serializer_class = TaskSerializer



# Task progress view
# View that displays the task progress page
@login_required     # Decorator ensuring that view is only accessible to logged-in users
def task_progress(request):
    return render(request, 'tasks/task_progress.html')  # Render the progress page


# Task progress data view
# View that returns task progress data (tasks completed and created) in a JSON format
@login_required     # Decorator ensuring that view is only accessible to logged-in users
def task_progress_data(request):
    # Determine time range for the data (default is set to week)
    filter_option = request.GET.get('filter', 'week')
    # Get today's date
    today = now().date()

    # Determine the date range
    if filter_option == 'month':
        # Show the past 30 days for month view
        date_range = [today - timedelta(days=i) for i in range(30)]
    else:  # Default to 'week'
        # Show the past 7 days for week view
        date_range = [today - timedelta(days=i) for i in range(7)]

    # Make sure date is in chronological order
    date_range.reverse()

    # Initialize task data
    task_data = {
        'dates': [day.strftime("%Y-%m-%d") for day in date_range],
        'completed': [],
        'created': [],
    }

    # Go through dates and gather data
    for day in date_range:
        # Filter database for completed tasks
        completed_count = Task.objects.filter(
            user=request.user,
            completed=True,
            completed_at__date=day
        ).count()
        # Filter database for created tasks
        created_count = Task.objects.filter(
            user=request.user,
            created_at__date=day
        ).count()
        # Append the counts to the respective lists
        task_data['completed'].append(completed_count)
        task_data['created'].append(created_count)

    # Send task_data dictionary back to frontend in JSON format
    return JsonResponse(task_data)


# Completed tasks view
# View that shows a list of completed tasks
def completed_tasks(request):
    # Filters database for completed tasks by logged-in user
    tasks = Task.objects.filter(user=request.user, completed=True)
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})  # Passes tasks to completed_tasks.html for display


# Complete task view
# View that marks a task as completed
def complete_task(request, task_id):
    # Make sure the task belongs to the logged-in user
    task = get_object_or_404(Task, id=task_id, user=request.user)
    # Mark the task as completed
    task.completed = True
    # Set the completion date
    task.completed_at = timezone.now()
    # Save the task
    task.save()
    return redirect('task_list')  # Redirect back to the task list


# Task list view
# View that displays all incomplete tasks for the logged-in user
@login_required     # Decorator ensuring that view is only accessible to logged-in users
def task_list(request):
    # Filters database for incomplete tasks for the user
    tasks = Task.objects.filter(user=request.user, completed=False)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})    # Passes tasks to the task_list.html for display


# Create task view
# View that handles task creation
@login_required     # Decorator ensuring that view is only accessible to logged-in users
def create_task(request):
    # Checks if request method is POST (form has been submitted)
    if request.method == 'POST':
        # Initializes the TaskForm with the data submitted via the POST request (request.POST)
        # Maps submitted data (task title and description) to the corresponding model fields
        form = TaskForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Creates a Task instance from the form data but doesn't save it to database yet
            task = form.save(commit=False)
            # Assigns current logged-in user as owner of the task (links task to the user who created it)
            task.user = request.user
            # Saves task instance to the database
            task.save()
            return redirect('task_list')    # Redirects to the task_list page after successfully creating a task
    # If request method isn't POST (form not submitted yet), create an empty TaskForm instance
    else:
        form = TaskForm()
    # Renders create_task.html and passes form instance as variable
    return render(request, 'tasks/create_task.html', {'form': form})
