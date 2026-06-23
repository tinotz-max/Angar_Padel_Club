from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourtViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'courts', CourtViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]