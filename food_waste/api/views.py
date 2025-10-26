from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import FoodItem, Donation
from .serializers import UserSerializer, FoodItemSerializer, DonationSerializer

User = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all().order_by('-created_at')
    serializer_class = FoodItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        # optional filters: owner, expires_before, location
        owner = self.request.query_params.get('owner')
        if owner:
            qs = qs.filter(owner__id=owner)
        return qs

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all().order_by('-created_at')
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def mark_picked_up(self, request, pk=None):
        donation = self.get_object()
        donation.picked_up = True
        from django.utils import timezone
        donation.picked_up_at = timezone.now()
        donation.save()
        return Response({'status': 'marked picked up'})

# Simple JWT views (re-exported for easier URL wiring)
class TokenObtainPairView(TokenObtainPairView):
    pass

class TokenRefreshView(TokenRefreshView):
    pass
