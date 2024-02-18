from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    raw_id_fields = ['product']  # Helps to search for a product in a large dataset

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_date', 'total_price', 'status']
    list_filter = ['status', 'order_date']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

