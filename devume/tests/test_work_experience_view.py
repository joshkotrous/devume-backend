from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


from devume.models.profile import Profile
from devume.models.work_experience import WorkExperience

class WorkExperienceViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.profile = Profile.objects.create(user=self.user)


    
    def test_get_work_experience(self):
        # Simulate login and get session cookie
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
 # Include session cookie in headers
        self.work_experience = WorkExperience.objects.create(profile=self.profile)
        response = self.client.get('/api/work_experience', headers=headers)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_create_work_experience(self):
        # Simulate login and get session cookie
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        response = self.client.post('/api/work_experience/create', headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_get_work_experience_for_user(self):
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'}

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        response = self.client.get(f'/api/work_experience/{self.profile.uuid}', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertNotIsInstance(response.json(), list)

    def test_update_work_experience(self):
        work_experience_data = {
            'birth_date':'2024-01-01',
            'bio': 'test',
        }
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'}
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.work_experience = WorkExperience.objects.create(profile=self.profile)
        response = self.client.put(f'/api/work_experience/update/{self.work_experience.uuid}', work_experience_data, format='json', headers=headers)
        self.assertEquals(response.status_code, 200)