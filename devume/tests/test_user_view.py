from django.contrib.auth.models import User
from django.test import TestCase, Client
import json

class UserViewTestCase(TestCase):
    # Setup test case
    # Built in function from Django
    def setUp(self):
        self.client = Client()

    def test_get_users(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        user_data = {
            'username': 'testuser122',
            'password': 'testPassword',
            'email': 'test@example.com'
        }

        response = self.client.post('/api/users/create', json.dumps(user_data), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'testuser122')

    # Test case tear down procedures
    # Built in function from Django
    def tearDown(self):
        return None