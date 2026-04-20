from django.urls import path
from .views import TourListAPIView, TourDetailAPIView, BookingCreateAPIView, BookingListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView # pyright: ignore[reportMissingImports]

urlpatterns = [
    path('tours/', TourListAPIView.as_view(), name='tour-list'),
    path('tours/<int:pk>/', TourDetailAPIView.as_view(), name='tour-detail'),
    path('bookings/', BookingCreateAPIView.as_view(), name='booking-create'),
    path('bookings/all/', BookingListAPIView.as_view(), name='booking-list'),
    path('api/accounts/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]