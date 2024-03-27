from django.urls import path
from . import views
from .views import add_to_wishlist, wishlist_detail

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', wishlist_detail, name='wishlist_detail'),
]
