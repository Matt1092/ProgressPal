# Defines the serializers for the tasks app in Django,
# transforming complex data types into native Python data types
# that can easily be rendered into JSON, XML, or other content types.
from rest_framework import serializers
from .models import Task

# Serializer class for the Task model
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task    # Associate this serializer with the Task model
        fields = ['id', 'title', 'description', 'completed', 'completed_at', 'created_at', 'user']
