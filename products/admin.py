from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'inventory', 'created_at', 'updated_at', 'image_display', 'edit_details_link']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'category']
    readonly_fields = ['image_preview'] 

    def image_display(self, obj):
        """Function to display product image in the admin list view."""
        if obj.image:
            return format_html('<img src="{}" style="width: 75px; height:auto;">', obj.image.url)
        return "No Image"
    image_display.short_description = "Image"

    def image_preview(self, obj):
        """Function to display an image preview in the product edit form."""
        if obj.image:
            return format_html('<img src="{}" style="width: 150px; height:auto;">', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

    def edit_details_link(self, obj):
        """Function to add a direct link to the product edit page from the list view."""
        url = reverse('admin:products_product_change', args=[obj.pk])
        return format_html('<a href="{}">Edit</a>', url)
    edit_details_link.short_description = 'Edit Details'

    def get_urls(self):
        """Override this method if you need to add custom views or urls."""
        urls = super().get_urls()
        return urls


