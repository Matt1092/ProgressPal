# Configures the tasks app in Django
from django.apps import AppConfig


class TasksConfig(AppConfig):
    # Sets default type for auto-incrementing primary keys to be a large 64-bit integer (BigAutoField)
    default_auto_field = "django.db.models.BigAutoField"
    # Defines Python path to tasks app, telling Django where to find it
    name = "tasks"
