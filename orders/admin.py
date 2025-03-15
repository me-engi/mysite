# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Category, Product, Cart, Order, OrderItem, Payment

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_shop_owner', 'is_customer', 'is_staff')
    list_filter = ('is_shop_owner', 'is_customer', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_shop_owner', 'is_customer', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_shop_owner', 'is_customer'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Profile Admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'city', 'state', 'country')
    list_filter = ('city', 'state', 'country')
    search_fields = ('user__username', 'phone_number', 'address')
    raw_id_fields = ('user',)

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')  # Add 'slug' to list_display
    prepopulated_fields = {'slug': ('name',)}  # This will now work



# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'shop_owner', 'price', 'stock', 'created_at')
    list_filter = ('category', 'shop_owner', 'created_at')
    search_fields = ('name', 'description')
    raw_id_fields = ('shop_owner', 'category')
    date_hierarchy = 'created_at'

# Cart Admin
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at')
    list_filter = ('user', 'added_at')
    search_fields = ('user__username', 'product__name')
    raw_id_fields = ('user', 'product')

# Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shop_owner', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'shop_owner')
    search_fields = ('user__username', 'shop_owner__username')
    raw_id_fields = ('user', 'shop_owner')
    date_hierarchy = 'created_at'

# OrderItem Admin
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_filter = ('order', 'product')
    search_fields = ('order__id', 'product__name')
    raw_id_fields = ('order', 'product')

# Payment Admin
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_method', 'status', 'paid_at')
    list_filter = ('status', 'payment_method', 'paid_at')
    search_fields = ('order__id', 'transaction_id')
    raw_id_fields = ('order',)
    date_hierarchy = 'paid_at'

# Register models with their respective admin classes
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)