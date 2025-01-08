# Defines a TaskForm which is integrated within Task model (simplifies creation and validation of tasks in my app), streamlining backend and frontend development
from django import forms    # Import forms module from Django (Provides access to Django's form-related classes and methods)
from .models import Task    # Import Task model from models.py (Allows forms.py to use Task model as basis for form)


# Define form class TaskForm that inherits from forms.modelForm
# Creates form tied to Task model
class TaskForm(forms.ModelForm):
    # Defines metadata for TaskForm class
    class Meta:
        # Indicates form is linked to Task model (the form will use Task model's to generate corresponding form fields)
        model = Task
        # Specifies which model fields should be included in the form (only title and description fields of Task model are rendered in the form)
        fields = ['title', 'description']
