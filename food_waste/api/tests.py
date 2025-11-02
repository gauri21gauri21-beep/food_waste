from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import FoodItem

User = get_user_model()

class BasicTests(TestCase):
    def test_create_fooditem(self):
        user = User.objects.create_user(username='tester', password='pass1234')
        self.client.login(username='tester', password='pass1234')
        resp = self.client.post('/api/fooditems/', {'title': 'Bananas', 'quantity': 3})
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(FoodItem.objects.count(), 1)
