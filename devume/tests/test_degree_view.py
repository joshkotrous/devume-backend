from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from devume.models.api_key import ApiKey

class DegreesViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_get_degrees_api_key_auth(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        response = self.client.get('/api/degrees', headers=headers)
        self.assertEqual(len(response.data), 4)

    def test_get_degrees_session_auth(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/degrees')
        self.assertEqual(len(response.data), 4)
