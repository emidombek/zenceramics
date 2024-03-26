from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Address, Wishlist
from orders.models import Order

@login_required
def profile_view(request):
    user = request.user
    orders = Order.objects.filter(user=user, status='Pending').order_by('-order_date')
    addresses = Address.objects.filter(user=user)
    wishlists = Wishlist.objects.filter(user=user)
    
    context = {
        'orders': orders,
        'addresses': addresses,
        'wishlists': wishlists,
    }
    return render(request, 'user/profile.html', context)

