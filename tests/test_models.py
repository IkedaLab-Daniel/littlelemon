from django.test import TestCase
from reservation.models import Menu

# ? To run this test: python3 manage.py test tests/


class MenuTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(
            title = "IceCream",
            price = 80,
            inventory = True
        )
        self.assertEqual(str(item), "IceCream : 80")
