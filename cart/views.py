from django.shortcuts import redirect, render
from .utils import add_to_cart, get_cart, remove_from_cart
from products.models import Product
from decimal import Decimal 

def cart_view(request):
    cart = request.session.get('cart', {})
    detailed_cart_items = []
    total_price = Decimal('0.00')  # Initialize as Decimal
    shipping_cost_per_item = Decimal('25.00')  # Use Decimal for consistent arithmetic operations

    total_items = sum(cart.values())  # Total number of items in the cart
    total_shipping_cost = total_items * shipping_cost_per_item  # Total shipping cost remains a Decimal

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_item_price = product.price * quantity  # This is already a Decimal because product.price is a Decimal
        total_price += total_item_price  # Both operands are Decimal now
        detailed_cart_items.append({
            'product_id': product_id,
            'name': product.name,
            'price': "{:.2f}".format(product.price),  # Formatting as string for display
            'quantity': quantity,
            'total_item_price': "{:.2f}".format(total_item_price),  # Formatting as string for display
            'image_url': product.image.url if product.image else None,
        })

    final_total = total_price + total_shipping_cost  # Calculation with Decimal

    context = {
        'cart_items': detailed_cart_items,
        'total_price': "{:.2f}".format(total_price),
        'total_shipping_cost': "{:.2f}".format(total_shipping_cost),
        'final_total': "{:.2f}".format(final_total),
    }

    return render(request, 'cart/cart_detail.html', context)

def add_to_cart_view(request, product_id):
    # This is a simplified add check for product existence, etc later on.
    add_to_cart(request, str(product_id), 1)  # Adding one product; adjust as needed
    return redirect('cart_view')

def remove_from_cart_view(request, product_id):
    remove_from_cart(request, str(product_id))
    return redirect('cart_view')
