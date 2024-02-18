from django.shortcuts import redirect, render
from .utils import add_to_cart, get_cart, remove_from_cart

def cart_view(request):
    cart = get_cart(request)
    # Optionally, resolve product IDs to actual Product instances to display more info
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def add_to_cart_view(request, product_id):
    # This is a simplified add check for product existence, etc later on.
    add_to_cart(request, str(product_id), 1)  # Adding one product; adjust as needed
    return redirect('cart_view')

def remove_from_cart_view(request, product_id):
    remove_from_cart(request, str(product_id))
    return redirect('cart_view')
