from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItem,Booking

# Create your serializers here
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"