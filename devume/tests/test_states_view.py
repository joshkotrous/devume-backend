from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from devume.models.state import State
from devume.models.country import Country
from devume.views.states_view import StatesCreateView, StatesListView, StatesRetrieveView, StatesUpdateView



class StatesViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.country = Country.objects.create(name='United States', country_code='US')
        self.state = State.objects.create(name='New York', state_code='NY', country_id=self.country.id)

    def test_get_states(self):
        # Simulate login and get session cookie
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
 # Include session cookie in headers
        response = self.client.get('/api/states', headers=headers)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_create_state(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
 # Include session cookie in headers
        state_data = {
            'name': 'California',
            'state_code': 'CA',
            'country': self.country.id
        }
        response = self.client.post('/api/states/create', state_data, format='json')
        self.assertEqual(response.status_code, 201)

