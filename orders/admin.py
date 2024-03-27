from django.contrib import admin
from .models import Order, OrderItem

def make_order_shipped(modeladmin, request, queryset):
    queryset.update(status='Shipped')
make_order_shipped.short_description = "Mark selected orders as shipped"

class OrderAdmin(admin.ModelAdmin):
    actions = [make_order_shipped]
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    raw_id_fields = ['product']  # Helps to search for a product in a large dataset

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_date', 'total_price', 'status']
    list_filter = ['status', 'order_date']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

