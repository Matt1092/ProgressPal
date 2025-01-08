# Defines the RESTful API URL routing for the tasks app in Django
# Imports necessary modules for URL routing
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Create a DefaultRouter instance for RESTful API routing
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')    # Register the UserViewSet with the router

# Define the URL patterns for the API endpoints
urlpatterns = [
    path('', include(router.urls)),    # Include the router-generated URLS
]
