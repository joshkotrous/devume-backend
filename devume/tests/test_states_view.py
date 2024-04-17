from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from devume.models.state import State
from devume.models.country import Country
from devume.models.api_key import ApiKey


class StatesViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.country = Country.objects.create(name='United States', country_code='US')
        self.state = State.objects.create(name='New York', state_code='NY', country_id=self.country.id)
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_list_states_session_auth(self):
        # Simulate login and get session cookie
        self.client.force_login(self.user)
        response = self.client.get('/api/states')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_list_states_api_key_auth(self):
        # Simulate login and get session cookie
        headers = {'x-api-key': str(self.apikey.key)} 
        response = self.client.get('/api/states', headers=headers)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_state_api_key_auth(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        response = self.client.get(f'/api/states/{self.state.id}', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_state_session_auth(self):
        self.client.force_login(self.user)
        response = self.client.get(f'/api/states/{self.state.id}')
        self.assertEqual(response.status_code, 200)


    def test_create_state(self):
        headers = {'x-api-key': str(self.apikey.key)} 

        state_data = {
            'name': 'California',
            'state_code': 'CA',
            'country': self.country.id
        }
        response = self.client.post('/api/states/create', state_data, format='json', headers=headers)
        self.assertEqual(response.status_code, 201)


    def test_update_state(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        state_data = {
            'name': 'California',
            'state_code': 'CA',
            'country': self.country.id
        }
        response = self.client.patch(f'/api/states/{self.state.id}/update', state_data, format='json', headers=headers)
        self.assertEqual(response.status_code, 200)

