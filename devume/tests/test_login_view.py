from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from devume.models.api_key import ApiKey


class LoginViewTestCase(APITestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_login(self):
        headers = {"x-api-key": str(self.apikey.key)}

        user_data = {
            "username": self.username,
            "password": self.password,
        }

        response = self.client.post("/api/login", user_data, format="json", headers=headers)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        return None
