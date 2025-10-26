from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'fooditems', views.FoodItemViewSet, basename='fooditem')
router.register(r'donations', views.DonationViewSet, basename='donation')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
