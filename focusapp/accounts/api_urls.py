# Defines the RESTful API URL routing for the accounts app in Django
# Imports necessary modules for URL routing
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet  # Import the UserViewSet from the views module

# Create a DefaultRouter instance for RESTful API routing
router = DefaultRouter()
router.register(r'users', UserViewSet)  # Register the UserViewSet with the router

# Define the URL patterns for the API endpoints
urlpatterns = [
    path('', include(router.urls)),     # Include the router-generated URLS
]
