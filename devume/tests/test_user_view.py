from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from devume.models.api_key import ApiKey

class UserViewTestCase(APITestCase):
    # Setup test case
    # Built in function from Django
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpassword"
        )
        self.apikey = ApiKey.objects.create(user=self.superuser)


    def test_list_users_session_auth(self):
        self.client.force_login(self.superuser)
        response = self.client.get("/api/users")
        self.assertEqual(response.status_code, 200)

    
    def test_list_users_api_key_auth(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        response = self.client.get("/api/users", headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_user_session_auth(self):
        self.client.force_login(self.superuser)
        response = self.client.get(f"/api/users/{self.superuser.id}")
        self.assertEqual(response.status_code, 200)

    def test_get_user_api_key_auth(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        response = self.client.get(f"/api/users/{self.superuser.id}", headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        user_data = {
            "username": "testuser122",
            "password": "testPassword",
            "email": "test@example.com",
        }

        response = self.client.post("/api/users/create", user_data, format="json", headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 2)

    def test_update_user(self):
        headers = {'x-api-key': str(self.apikey.key)}
        self.client.force_login(self.superuser)
        user_data = {
            "username": "testuser122",
            "password": "testPassword",
            "email": "test@example.com",
        }
        update_user_data = {
            "username": "testuser122",
            "email": "test2024@example.com",
            "first_name": "test",
            "last_name": "test"
        }
        response = self.client.post("/api/users/create", user_data, format="json", headers=headers)
        response2 = self.client.patch('/api/users/' + str(response.data['id']) + '/update', update_user_data, format='json')
        self.assertEquals(response2.status_code, 200)
        self.assertEquals(response2.data['first_name'], update_user_data['first_name'])
        self.assertEquals(response2.data['last_name'], update_user_data['last_name'])

    def tearDown(self):
        return None
