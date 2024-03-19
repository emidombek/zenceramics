from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html' 
    context_object_name = 'products'
    paginate_by = 10  
    ordering = ['name']  

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)
        return queryset

def ProductDetailView(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    response_data = {
        'name': product.name,
        'image': product.image.url if product.image else None,
        'description': product.description,
        'price': product.price,
    }
    return JsonResponse(response_data)