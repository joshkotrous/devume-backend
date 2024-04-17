from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from devume.models.profile import Profile
from devume.models.work_experience import WorkExperience
from devume.models.api_key import ApiKey
class WorkExperienceViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.profile = Profile.objects.create(user=self.user)
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_list_work_experience_session_auth(self):
        self.client.force_login(self.user)
        self.work_experience = WorkExperience.objects.create(profile=self.profile)
        response = self.client.get('/api/work_experience')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_list_work_experience_api_key_auth(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        self.work_experience = WorkExperience.objects.create(profile=self.profile)
        response = self.client.get('/api/work_experience', headers=headers)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_work_experience_for_user_session_auth(self):
        self.client.force_login(self.user)
        self.client.post('/api/work_experience/create')
        self.client.post('/api/work_experience/create')
        response = self.client.get(f'/api/work_experience/{self.profile.uuid}')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_work_experience_for_user_api_key_auth(self):
        headers = {'x-api-key': str(self.apikey.key)} 
        self.client.post('/api/work_experience/create', headers=headers)
        self.client.post('/api/work_experience/create', headers=headers)
        response = self.client.get(f'/api/work_experience/{self.profile.uuid}', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_work_experience(self):
        self.client.force_login(self.user)
        response = self.client.post('/api/work_experience/create')
        self.assertEqual(response.status_code, 201)

    def test_update_work_experience(self):
        self.client.force_login(self.user)
        work_experience_data = {
            'start_date':'2024-01-01',
            'company': 'test',
        }
        self.work_experience = WorkExperience.objects.create(profile=self.profile)
        response = self.client.patch(f'/api/work_experience/{self.work_experience.id}/update', work_experience_data, format='json')
        self.assertEquals(response.status_code, 200)