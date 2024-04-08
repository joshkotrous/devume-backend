
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class LoginViewTestCase(APITestCase):
  # Built in function from Django
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)


    def test_login(self):
        user_data = {
            'username': self.username,
            'password': self.password,
        }

        response = self.client.post('/api/login', user_data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('session_id', response.data)

    # Test case tear down procedures
    # Built in function from Django
    def tearDown(self):
        return None