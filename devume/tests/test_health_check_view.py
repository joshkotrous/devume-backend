from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from devume.models.api_key import ApiKey


class HealthCheckViewTestCase(APITestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_health_check(self):
        headers = {"x-api-key": str(self.apikey.key)}
        response = self.client.get("/api/health", headers=headers)
        self.assertEqual(response.status_code, 200)
