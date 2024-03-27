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
    return render(request, 'users/profile.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Wishlist
from .forms import WishlistForm

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.product = product
            wishlist_item.save()
            return redirect('wishlist_detail') 
    else:
        form = WishlistForm()
    return render(request, 'add_to_wishlist.html', {'form': form, 'product': product})
