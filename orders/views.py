from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from products.models import Product
from cart.utils import get_cart, clear_cart, get_cart_total_price #changing from class to util func

@login_required
def order_create(request):
    cart_items = get_cart(request)
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address', 'Default Address')
        
        # Assume get_cart_total_price returns the total price for the cart
        total_price = get_cart_total_price(request)
        
        order = Order.objects.create(
            user=request.user, 
            shipping_address=shipping_address, 
            total_price=total_price,
            status='Pending'  # or any default status you prefer
        )
        
        # Loop through the cart items and create an OrderItem for each
        for item_id, item_data in cart_items.items():
            product = Product.objects.get(id=item_id)
            OrderItem.objects.create(
                order=order, 
                product=product, 
                quantity=item_data['quantity'], 
                price=product.price  # This assumes the price is stored with the product
            )

        clear_cart(request)  # Clear the session cart
        return redirect('order_detail', order_id=order.id)

    # If GET request or the form hasn't been submitted yet
    return render(request, 'orders/order_create.html', {'cart': cart_items})


