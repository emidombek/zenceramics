from django.shortcuts import redirect, render
from .utils import add_to_cart, get_cart, remove_from_cart
from products.models import Product
from decimal import Decimal 
from django.http import HttpResponseRedirect
from .forms import ShippingForm, PaymentForm
from django.contrib import messages
from .models import Order, OrderItem
from products.models import Product

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

def update_cart_view(request, product_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 0)
        try:
            quantity = int(quantity)
            if quantity > 0:
                # Update the quantity in the session cart
                cart = request.session.get('cart', {})
                cart[str(product_id)] = quantity
                request.session['cart'] = cart
            else:
                # Remove the item if the quantity is 0 or less
                remove_from_cart(request, str(product_id))
        except ValueError:
            # Handle the exception if quantity is not an integer
            pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('products:product_list')
    
    if request.method == 'POST':
        shipping_form = ShippingForm(request.POST)
        payment_form = PaymentForm(request.POST)
        if shipping_form.is_valid() and payment_form.is_valid():
            address = shipping_form.save(commit=False)
            address.user = request.user
            address.save()

            # Assume you have a function to calculate total price from cart
            total_price = calculate_cart_total(cart)

            order = Order.objects.create(user=request.user, total_price=total_price, shipping_address=address)
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)
            
            # Insert stripe payment processing here 

            request.session['cart'] = {}  # Clear the cart
            messages.success(request, "Your order has been placed.")
            return redirect('order_success')
    else:
        shipping_form = ShippingForm()
        payment_form = PaymentForm()

    return render(request, 'cart/checkout.html', {'shipping_form': shipping_form, 'payment_form': payment_form})
