from django.urls import path
from .views import about_view  # Import your view function

app_name = 'support'

urlpatterns = [
    path('about/', about_view, name='about'),
]