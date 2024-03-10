from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductListByCategoryView(ListView):
    model = Product
    template_name = 'products/product_list.html' 

    def get_queryset(self):
        """Filter products by category."""
        category = self.kwargs.get('category')
        return Product.objects.filter(category__iexact=category)