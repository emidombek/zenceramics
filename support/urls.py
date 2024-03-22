from django.urls import path
from .views import about_view  # Import your view function

urlpatterns = [
    path('about/', about_view, name='about'),
]