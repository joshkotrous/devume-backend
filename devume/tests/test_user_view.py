from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class UserViewTestCase(APITestCase):
    # Setup test case
    # Built in function from Django
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword')
        self.token = Token.objects.create(user=self.superuser)

    def test_get_users(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        user_data = {
            'username': 'testuser122',
            'password': 'testPassword',
            'email': 'test@example.com'
        }

        response = self.client.post('/api/users/create', user_data,format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 2)
        # self.assertEqual(User.objects.first().username, 'testuser122')

    # Test case tear down procedures
    # Built in function from Django
    def tearDown(self):
        return None