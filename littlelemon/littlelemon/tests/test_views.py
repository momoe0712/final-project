from rest_framework.test import APITestCase, APIClient
from myapp.models import Menu
from myapp.serializers import menuSerializer

class MenuViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(Title="Pizza", Price=12, Inventory=5)

    def test_getall(self):
        response = self.client.get('/menu/')  # Use the correct URL
        items = Menu.objects.all()
        serialized = menuSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)

