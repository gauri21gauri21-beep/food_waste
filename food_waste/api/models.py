from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FoodItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_items')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=1)
    expires_at = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} (x{self.quantity})"

class Donation(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='donations')
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations_made')
    recipient_contact = models.CharField(max_length=255, blank=True)
    picked_up = models.BooleanField(default=False)
    picked_up_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation of {self.food_item.title} by {self.donor.username}"        