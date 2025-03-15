# serializers.py
from rest_framework import serializers
from .models import User, Profile, Category, Product, Cart, Order, OrderItem, Payment

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_shop_owner', 'is_customer']
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is write-only
        }

    def create(self, validated_data):
        # Create a new user with the validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_shop_owner=validated_data.get('is_shop_owner', False),
            is_customer=validated_data.get('is_customer', False)
        )
        return user

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'phone_number', 'address', 'city', 'state', 'country', 'postal_code', 'profile_picture', 'shop_name', 'shop_address', 'shop_description']

    def update(self, instance, validated_data):
        # Update nested User data
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.email = user_data.get('email', user.email)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.is_shop_owner = user_data.get('is_shop_owner', user.is_shop_owner)
            user.is_customer = user_data.get('is_customer', user.is_customer)
            user.save()

        # Update Profile data
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.shop_name = validated_data.get('shop_name', instance.shop_name)
        instance.shop_address = validated_data.get('shop_address', instance.shop_address)
        instance.shop_description = validated_data.get('shop_description', instance.shop_description)
        instance.save()

        return instance

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'shop_owner', 'image', 'created_at', 'updated_at']

# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity', 'added_at']

# OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # Nested serializer for order items

    class Meta:
        model = Order
        fields = ['id', 'user', 'shop_owner', 'total_price', 'created_at', 'status', 'items']

# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'payment_method', 'transaction_id', 'paid_at', 'status']