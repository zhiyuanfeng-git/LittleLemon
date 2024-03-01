from django.test import TestCase
from restaurant.models import MenuItem,Booking

# Create your tests here
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="TestItem1", price=19.8, inventory=1000)
        self.assertEqual(item.title, "TestItem1")