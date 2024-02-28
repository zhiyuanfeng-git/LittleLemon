from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer

# Create your views here.
class IndexView(generics.ListAPIView):
    def get(self,request):
        return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

