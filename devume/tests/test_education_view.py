from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from devume.models.education import Education
from devume.models.profile import Profile

class EducationViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.profile = Profile.objects.create(user=self.user)

    def test_get_education(self):
        # Simulate login and get session cookie
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        # Include session cookie in headers
        self.education = Education.objects.create(profile=self.profile)
        response = self.client.get('/api/education', headers=headers)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_education(self):
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        # Include session cookie in headers
        self.education = Education.objects.create(profile=self.profile)
        self.education = Education.objects.create(profile=self.profile)
        response = self.client.get(f'/api/education/{self.profile.uuid}', headers=headers)
        self.assertEqual(len(response.data), 2)

    def test_update_education(self):
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        # Include session cookie in headers
        self.education = Education.objects.create(profile=self.profile)
        education_data = {
            'degree': 'Bachelors',
            'school_name': 'NYU'
        }
        response = self.client.patch(f'/api/education/{self.education.id}/update', education_data, headers=headers)
        self.assertEqual(response.data['school_name'], education_data['school_name'])
        self.assertEqual(response.data['degree'], education_data['degree'])

    def test_create_education(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        education_data = {
            'degree': 'Bachelors',
            'school_name': 'NYU'
        }
        response = self.client.post('/api/education/create', education_data)
        print(response.data)
        self.assertEqual(response.status_code, 201)


