from django.urls import path
from .views import order_create, OrderDetailView, OrderListView

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('detail/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('my_orders/', OrderListView.as_view(), name='my_orders'),
]