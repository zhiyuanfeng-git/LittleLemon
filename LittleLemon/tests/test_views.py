from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from restaurant.models import MenuItem,Booking
from restaurant.serializers import MenuItemSerializer
    
# Create your tests here
class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="test_item_1",price=123,inventory=10000)
        MenuItem.objects.create(title="test_item_2",price=223,inventory=10001)
        MenuItem.objects.create(title="test_item_3",price=323,inventory=10002)
    
    def test_all_menuitems(self):
        client = APIClient()
        response = client.get('/menu/')
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items,many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)