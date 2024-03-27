from django import forms
from .models import Address,Wishlist

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'address_line_1', 'address_line_2', 'city', 'state_province_region', 'postal_zip_code', 'country', 'phone', 'is_default']

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['product', 'notes', 'quantity']
        widgets = {'notes': forms.Textarea(attrs={'cols': 40, 'rows': 5})}
