from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from devume.models.city import City
from devume.models.country import Country
from devume.models.state import State
from devume.views.cities_view import CitiesCreateView, CitiesListView, CitiesRetrieveView, CitiesUpdateView



class CitiesViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.country = Country.objects.create(name='United States', country_code='US')
        self.state = State.objects.create(name="New York", country_id=self.country.id)
        self.city = City.objects.create(name='New York City', state_id=self.state.id)

    def test_get_cities(self):
        # Simulate login and get session cookie
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
 # Include session cookie in headers
        response = self.client.get('/api/cities', headers=headers)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_create_city(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
 # Include session cookie in headers
        city_data = {
            'name': 'Albany',
            'state': 0
        }
        response = self.client.post('/api/cities/create', city_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], city_data['name'])
        self.assertEqual(response.data['state'], city_data['state'])


