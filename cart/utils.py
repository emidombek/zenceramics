from decimal import Decimal
from products.models import Product

def get_cart(request):
    return request.session.get('cart', {})

def add_to_cart(request, product_id, quantity):
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    request.session['cart'] = cart

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']

def calculate_cart_total(cart):
    total = Decimal('0.00')
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total += product.price * Decimal(quantity)
    return total
