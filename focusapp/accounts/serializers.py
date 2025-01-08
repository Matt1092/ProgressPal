# Defines the serializers for the accounts app in Django,
# transforming complex data types into native Python data types
# that can easily be rendered into JSON, XML, or other content types.
from rest_framework import serializers
from django.contrib.auth.models import User

# Serializer class for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User    # Associate this serializer with the User model
        # Added password in fields to show the password hashing
        fields = ['id', 'username', 'email', 'password']
