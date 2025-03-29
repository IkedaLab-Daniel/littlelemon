from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from reservation.models import Menu
from reservation.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient() 
        self.item1 = Menu.objects.create(title="Pizza", price=150, inventory=True)

    def test_getall(self):
        response = self.client.get(reverse("menu-list"))  # Call the API endpoint
        menu_items = Menu.objects.all()  # Get all items from DB
        serializer = MenuSerializer(menu_items, many=True)  # Serialize the data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)  
