from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'address_line_1', 'address_line_2', 'city', 'state_province_region', 'postal_zip_code', 'country', 'phone', 'is_default']