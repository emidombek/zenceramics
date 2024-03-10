from django.urls import path
from .views import ProductListView, ProductDetailView, ProductListByCategoryView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:category>/', ProductListByCategoryView.as_view(), name='product_list_by_category'),
]