from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Product, Customer, Cart, Payment, OrderPlaced


# Register your models here.


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'state', 'locality', 'mobile']
    search_fields = ['user', 'name']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    fields_sets = ['title','discounting_price','category','product_image']
    list_display = ['title', 'discounting_price', 'category', 'product_image']
    search_fields = ['title', 'category']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    search_fields = ['user', 'product']


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id']
    search_fields = ['user', 'razorpay_order_id']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date']
    search_fields = ['id', 'user', 'customer', 'product', 'quantity']
