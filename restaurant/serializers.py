from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

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
        fields = ['name', 'no_of_guests', 'date', 'slot']

        validators = [
            UniqueTogetherValidator(
                queryset=Booking.objects.all(),
                fields=['name','date','slot'],
                message='data duplication'
            )
        ]