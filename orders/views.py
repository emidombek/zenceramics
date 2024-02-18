from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.cart import Cart  # Assuming you have a Cart class to manage cart items

@login_required
def order_create(request):
    cart = Cart(request)  # Load the cart
    if request.method == 'POST':
        # Process form submission, e.g., shipping address from request.POST
        order = Order.objects.create(user=request.user, shipping_address='Address', total_price=cart.get_total_price())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['price'])
        # Clear the cart
        cart.clear()
        # Redirect to the payment or order confirmation page
        return redirect('order_detail', order_id=order.id)
    # Render order form page
    return render(request, 'orders/order_create.html', {'cart': cart})

