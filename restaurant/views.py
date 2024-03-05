from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
import json

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.parsers import JSONParser
from django.core import serializers as django_serializers

from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer

from .data_pickup.pickup_about import pickup_about

# Create your views here.
class IndexView(APIView):
    def get(self,request):
        return render(request, 'index.html', {})

class AboutView(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]

    def get(self,request):
        # In the production environment, there may not be a need for the follow code.
        # Here only is for testing some concepts.
        list_data = pickup_about.get_list()
        caption = pickup_about.get_caption()
        about_us = pickup_about.get_readme()
        return Response({'data': list_data, 'about_us': about_us, 'caption': caption},template_name='about.html')

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
    #permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    parser_classes = [JSONParser]

    def list(self,request):
        return Response({},template_name="book.html")

    def create(self,request):
        date = request.data.get('date')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        json_data = self.buildRetrieveData(date)
        return HttpResponse(json_data, content_type='application/json')
    
    def retrieve(self,request):
        date = request.GET.get('date')
        json_data = self.buildRetrieveData(date)
        return HttpResponse(json_data, content_type='application/json')
    
    def buildRetrieveData(self,date):
        bookings = Booking.objects.all().filter(date=date)
        serializer = BookingSerializer(bookings,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return json_data
    
class Reservations(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bookings.html'
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self,request):
        #[TODO]filter and pagination
        bookings = self.get_queryset()
        serializer = BookingSerializer(bookings,many=True)
        json_data = json.dumps(serializer.data)
        return Response({'bookings_data': json_data})