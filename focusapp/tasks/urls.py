# Defines the URL routing for the tasks app in Django
# Maps URLs to specific view functions that handle the logic for each URL
from django.urls import path, include                                                                                    # Path function to define URL patterns
from .views import task_list, create_task, complete_task, completed_tasks, task_progress_data, task_progress    # View functions from the views.py file


# Defines a list of URL patterns for this app
urlpatterns = [
    path('', task_list, name='task_list'),                                      # Maps root URL to the task_list view function
    path('create/', create_task, name='create_task'),                           # Maps URL /create/ to the create_task view function
    path('complete/<int:task_id>/', complete_task, name='complete_task'),       # Maps URL /complete/<int:task_id> to the complete_task view function
    path('completed/', completed_tasks, name='completed_tasks'),                # Maps URL /completed/ to the completed_tasks view function
    path('task_progress_data/', task_progress_data, name='task_progress_data'), # Maps URL /task_progress_data/ to the task_progress_data view function
    path('task_progress/', task_progress, name='task_progress'),                # Maps URL /task_progress/ to the task_progress view function
]
