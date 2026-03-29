from django.contrib import admin
from .models import Tour, Booking


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'city', 'price', 'duration', 'available_slots')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'tour', 'people_count', 'travel_date', 'created_at')