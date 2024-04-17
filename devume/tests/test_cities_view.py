from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from devume.models.city import City
from devume.models.country import Country
from devume.models.state import State
from devume.models.api_key import ApiKey


class CitiesViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.country = Country.objects.create(name='United States', country_code='US')
        self.state = State.objects.create(name="New York", country_id=self.country.id)
        self.city = City.objects.create(name='New York City', state_id=self.state.id)
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_cities_list_api_key_auth(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        response = self.client.get('/api/cities', headers=headers)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_cities_list_session_auth(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/cities')
        print(response.data)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_create_city(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        city_data = {
            'name': 'Albany',
            'state': self.state.id
        }
        response = self.client.post('/api/cities/create', city_data, format='json', headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], city_data['name'])
        self.assertEqual(response.data['state'], city_data['state'])

    def test_update_city(self):
        self.city = City.objects.create(name='Albany', state=self.state)
        headers = {'x-api-key': str(self.apikey.key)} 
        city_data = {
            'name': 'Rochester',
            'state': self.state.id
        }
        response = self.client.patch(f'/api/cities/{self.city.id}/update', city_data, format='json', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], city_data['name'])
        self.assertEqual(response.data['state'], city_data['state'])


