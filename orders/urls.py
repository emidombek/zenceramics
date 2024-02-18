from django.urls import path
from .views import order_create, OrderDetailView, OrderListView
from . import views

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('my_orders/', OrderListView.as_view(), name='my_orders'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]