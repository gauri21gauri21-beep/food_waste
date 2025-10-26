from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import FoodItem, Donation

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)

class FoodItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = FoodItem
        fields = '__all__'
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')

class DonationSerializer(serializers.ModelSerializer):
    donor = UserSerializer(read_only=True)
    food_item = FoodItemSerializer(read_only=True)
    food_item_id = serializers.PrimaryKeyRelatedField(
        queryset=FoodItem.objects.all(), source='food_item', write_only=True
    )
    class Meta:
        model = Donation
        fields = ('id', 'food_item', 'food_item_id', 'donor', 'recipient_contact', 'picked_up', 'picked_up_at', 'created_at')
        read_only_fields = ('id', 'donor', 'created_at', 'food_item')
