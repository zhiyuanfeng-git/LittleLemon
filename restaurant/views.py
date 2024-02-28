from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import generics

from .models import MenuItem
from .serializers import MenuItemSerializer

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