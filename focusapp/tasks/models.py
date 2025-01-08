# Defines database structure for tasks app (uses Django's ORM to represent database tables as Python classes) which makes the working with data aspect easier
# When running python manage.py makemigrations and migrate, Django translates model into SQL commands to create a table in the database
# Each Task object is a row in the table and Task model enables CRUD operations on tasks through ORM
# Imports necessary tools to define database models in Django
from django.db import models                # Models from Django to create database tables (models)
from django.contrib.auth.models import User # User to use the built-in user authentication model
from django.utils import timezone           # For handling date and time


# Define Task class (corresponds to a database table named tasks_task by default (app name + model name ))
class Task(models.Model):
    # Short string field with max length 200 to store task's title (maps to VARCHAR(200) in the database)
    title = models.CharField(max_length=200)
    # Large text field for descriptions of the task (maps to TEXT column in the database)
    description = models.TextField()
    # Boolean field to track whether or not the task is completed
    completed = models.BooleanField(default=False)
    # Datetime field to record when the task was completed
    completed_at = models.DateTimeField(null=True, blank=True)
    # Stores timestamp when task is created at
    created_at = models.DateTimeField(default=timezone.now)
    # Foreign key to link the task to a specific user (makes sure that when user is deleted, all their tasks are also deleted)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    # Method that defines what is displayed when the object is converted to a string
    def __str__(self):
        return self.title
