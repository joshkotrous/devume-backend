from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from devume.models.skill import Skill
from devume.models.api_key import ApiKey


class SkillViewTestCase(APITestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_list_skills_session_auth(self):
        self.client.force_login(self.user)
        self.skills = Skill.objects.create(name="Python")
        response = self.client.get("/api/skills")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_list_skills_api_key_auth(self):
        headers = {"x-api-key": str(self.apikey.key)}
        self.skills = Skill.objects.create(name="Python")
        response = self.client.get("/api/skills", headers=headers)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_skill_session_auth(self):
        self.client.force_login(self.user)
        self.skills = Skill.objects.create(name="Python")
        response = self.client.get(f"/api/skills/{self.skills.id}")
        self.assertEqual(response.status_code, 200)

    def test_get_skill_api_key_auth(self):
        headers = {"x-api-key": str(self.apikey.key)}
        self.skills = Skill.objects.create(name="Python")
        response = self.client.get(f"/api/skills/{self.skills.id}", headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_create_skill_session_auth(self):
        self.client.force_login(self.user)
        skill_data = {"name": "Python"}
        response = self.client.post("/api/skills/create", skill_data)
        self.assertEqual(response.status_code, 201)

    def test_create_skill_api_key_auth(self):
        headers = {"x-api-key": str(self.apikey.key)}
        skill_data = {"name": "Python"}
        response = self.client.post("/api/skills/create", skill_data, headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_update_skill(self):
        headers = {"x-api-key": str(self.apikey.key)}
        self.skills = Skill.objects.create(name="Python")
        skill_data = {"name": "JavaScript"}
        response = self.client.patch(
            f"/api/skills/{self.skills.id}/update", skill_data, headers=headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], skill_data["name"])
