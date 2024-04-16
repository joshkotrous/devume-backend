
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token



class LoginViewTestCase(APITestCase):
  # Built in function from Django
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)



    def test_login(self):
        user_data = {
            'username': self.username,
            'password': self.password,
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        response = self.client.post('/api/login', user_data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('session_id', response.data)

    # Test case tear down procedures
    # Built in function from Django
    def tearDown(self):
        return None