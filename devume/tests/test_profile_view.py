from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


from devume.models.profile import Profile

class ProfileViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.username2 = 'test_user2'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user2 = User.objects.create_user(username=self.username2, password=self.password)
        self.token = Token.objects.create(user=self.user)



    
    def test_get_profiles(self):
        # Simulate login and get session cookie
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
 # Include session cookie in headers
        self.profile = Profile.objects.create(user=self.user)
        self.profile = Profile.objects.create(user=self.user2)
        response = self.client.get('/api/profiles', headers=headers)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, 200)

    def test_create_profile(self):
        # Simulate login and get session cookie
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        response = self.client.post('/api/profiles/create', headers=headers)
        profiles = Profile.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(profiles), 1)

    def test_get_profile(self):
        self.client.force_login(self.user)
        self.profile = Profile.objects.create(user=self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'}

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        response = self.client.get(f'/api/profiles/{self.profile.uuid}', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertNotIsInstance(response.json(), list)

    def test_update_profile(self):
        profile_data = {
            'birth_date':'2024-01-01',
            'bio': 'test',
            'skills': '{[1, 2, 3]}'
        }
        self.client.force_login(self.user)
        self.profile = Profile.objects.create(user=self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'}
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        response = self.client.put(f'/api/profiles/update/{self.profile.uuid}', profile_data, format='json', headers=headers)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['birth_date'], profile_data['birth_date'])
        self.assertEquals(response.json()['bio'], profile_data['bio'])
        self.assertEquals(response.json()['skills'], profile_data['skills'])

    
    def test_update_profile_unauth(self):
        profile_data = {
            'birth_date':'2024-01-01',
            'bio': 'test',
        }

        self.profile = Profile.objects.create(user=self.user)
        response = self.client.put(f'/api/profiles/update/{self.profile.uuid}', profile_data, format='json')
        self.assertEquals(response.status_code, 401)


