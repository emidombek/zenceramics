from django.shortcuts import redirect, render
from .utils import add_to_cart, get_cart, remove_from_cart
from products.models import Product

def cart_view(request):
    cart = request.session.get('cart', {})
    detailed_cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_item_price = product.price * quantity
        total_price += total_item_price
        detailed_cart_items.append({
            'product_id': product_id,
            'name': product.name,
            'price': product.price,
            'quantity': quantity,
            'total_item_price': total_item_price,
            'image_url': product.image.url if product.image else None,  
        })

    return render(request, 'cart/cart_detail.html', {'cart_items': detailed_cart_items, 'total_price': total_price})

def add_to_cart_view(request, product_id):
    # This is a simplified add check for product existence, etc later on.
    add_to_cart(request, str(product_id), 1)  # Adding one product; adjust as needed
    return redirect('cart_view')

def remove_from_cart_view(request, product_id):
    remove_from_cart(request, str(product_id))
    return redirect('cart_view')
