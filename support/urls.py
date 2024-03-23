from django.urls import path
from .views import about_view
from .views import contact_view 

app_name = 'support'

urlpatterns = [
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]