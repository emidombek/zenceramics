from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html' 
    context_object_name = 'products'
    paginate_by = 10  # Or any number you prefer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'