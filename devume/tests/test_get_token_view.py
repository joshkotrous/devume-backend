from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class GetTokenViewTestCase(APITestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_get_token_view(self):
        user_data = {"username": self.username, "password": self.password}
        response = self.client.post("/api/token", user_data, format="json")
        self.assertEqual(response.status_code, 200)
