from rest_framework import serializers
from .models import Tour, Booking


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate_people_count(self, value):
        if value < 1:
            raise serializers.ValidationError("People count must be at least 1.")
        return value

    def validate_client_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Client name is too short.")
        return value