from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from devume.models.skill import Skill



class SkillViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)

    def test_list_skills(self):
        # Simulate login and get session cookie
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
 # Include session cookie in headers
        self.skills = Skill.objects.create(name='Python')
        response = self.client.get('/api/skills', headers=headers)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_skill(self):
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
 # Include session cookie in headers
        self.skills = Skill.objects.create(name='Python')
        response = self.client.get(f'/api/skills/{self.skills.id}', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_create_skill(self):
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
 # Include session cookie in headers
        skill_data = {
            'name': 'Python'
        }
        response = self.client.post(f'/api/skills/create', skill_data, headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_update_skill(self):
        self.client.force_login(self.user)
        session_cookie = self.client.cookies['sessionid'].value
        headers = {'Cookie': f'sessionid={session_cookie}'} 
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.skills = Skill.objects.create(name='Python')

 # Include session cookie in headers
        skill_data = {
            'name': 'JavaScript'
        }
        response = self.client.patch(f'/api/skills/{self.skills.id}/update', skill_data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], skill_data['name'])
