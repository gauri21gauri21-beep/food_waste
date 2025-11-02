from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'fooditems', api_views.FoodItemViewSet, basename='fooditem')
router.register(r'donations', api_views.DonationViewSet, basename='donation')
router.register(r'users', api_views.UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', api_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', api_views.TokenRefreshView.as_view(), name='token_refresh'),
]
