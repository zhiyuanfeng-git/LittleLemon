from django.shortcuts import render

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer

from .data_pickup.pickup_about import pickup_about

# Create your views here.
class IndexView(APIView):
    def get(self,request):
        return render(request, 'index.html', {})

class AboutView(APIView):
    def get(self,request):
        # In the production environment, there may not be a need for the follow code.
        # Here only is for testing some concepts.
        list_data = pickup_about.get_list()
        caption = pickup_about.get_caption()
        about_us = pickup_about.get_readme()
        return render(request, 'about.html', {'data': list_data, 'about_us': about_us, 'caption': caption})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def list(self, request):
        return render(request, 'menu.html', {'data':"test menu"})

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]