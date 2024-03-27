from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Product,Review



class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'  # Ensure this matches your actual template path
    context_object_name = 'products'
    paginate_by = 10  
    ordering = ['name']  

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        query = self.request.GET.get('q')

        if category:
            queryset = queryset.filter(category__iexact=category)

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__icontains=query)
            )

        return queryset

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        product_data = {
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'inventory': product.inventory,
            'image': product.image.url if product.image else None,
            'created_at': product.created_at,
            'updated_at': product.updated_at,
        }
     # Add reviews to the response data
        reviews_data = [{
            'user': review.user.username,
            'rating': review.rating,
            'comment': review.comment,
            'created_at': review.created_at
        } for review in reviews_data]

        # Combine product data and reviews into a single response
        response_data = {
            'product': product_data,
            'reviews': reviews_data,
        }

        return JsonResponse(response_data)