from django.test import TestCase
from .models import Menu, Booking
from .serializers import MenuSerializer

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Sorpa", price=5, inventory=100)
        self.assertEqual(item.title, "Sorpa")
        self.assertEqual(item.price, 5)
        self.assertEqual(item.inventory, 100)


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Sorpa", price=5, inventory=100)
        
    def test_getail(self):
        menu_items = Menu.objects.all()
        serialized_data = MenuSerializer(menu_items, many=True).data
        self.assertTrue(serialized_data)
        