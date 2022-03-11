from math import prod
from django.contrib import admin
from .models import Product, Collection, Promotion, Customer, Order, OrderItem, Address, Cart, CartItem
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ["clear_inventory"]
    list_display = ["title", "unit_price", "collection_title", "stock_status"]
    list_filter = ["collection", "last_update"]
    list_editable = ["unit_price"]
    search_fields = ["title__istartswith"]
    autocomplete_fields = ["collection"]
    prepopulated_fields = {
        "slug": ["title"]
    }

    list_select_related = ["collection"]

    def collection_title(self, product):
        return product.collection.title

    @admin.action(description="Clear Inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(stock=0)
        self.message_user(
            request,
            f"{updated_count} products were successsfully updated."
        )

    @admin.display(ordering="stock")
    def stock_status(self, product):
        if product.stock < 10:
            return "Low"
        else:
            return "OK"


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 20
    search_fields = ["first_name__istartswith", "last_name__istartswith"]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    min_num = 1
    max_num = 10
    autocomplete_fields = ["product"]
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "payment_status", "customer_name"]
    inlines = [OrderItemInline]
    list_select_related = ["customer"]
    autocomplete_fields = ["customer"]

    def order_id(self, order):
        return order.pk

    def customer_name(self, order):
        return f"{order.customer.first_name} {order.customer.last_name}"


class CartItemInline(admin.TabularInline):
    model = CartItem
    min_num = 1
    autocomplete_fields = ["product"]
    extra = 0


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display = ["cart_id", "created_at"]
    inlines = [CartItemInline]

    def cart_id(self, cart):
        return cart.pk


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "featured_product"]
    search_fields = ["title"]
