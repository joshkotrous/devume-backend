from rest_framework.test import APITestCase
from django.contrib.auth.models import User


from devume.models.profile import Profile
from devume.models.api_key import ApiKey


class ProfileViewTestCase(APITestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.username2 = "test_user2"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user2 = User.objects.create_user(username=self.username2, password=self.password)
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_profiles_list_session_auth(self):
        self.client.force_login(self.user)
        self.profile = Profile.objects.create(user=self.user)
        self.profile = Profile.objects.create(user=self.user2)
        response = self.client.get("/api/profiles")
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, 200)

    def test_profiles_list_api_key_auth(self):
        headers = {"x-api-key": str(self.apikey.key)}
        self.profile = Profile.objects.create(user=self.user)
        self.profile = Profile.objects.create(user=self.user2)
        response = self.client.get("/api/profiles", headers=headers)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, 200)

    def test_create_profile(self):
        headers = {"x-api-key": str(self.apikey.key)}
        response = self.client.post("/api/profiles/create", headers=headers)
        profiles = Profile.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(profiles), 1)

    def test_get_profile_session_auth(self):
        self.client.force_login(self.user)
        self.profile = Profile.objects.create(user=self.user)
        response = self.client.get(f"/api/profiles/{self.profile.uuid}")
        self.assertEqual(response.status_code, 200)
        self.assertNotIsInstance(response.json(), list)

    def test_get_profile_api_key_auth(self):
        headers = {"x-api-key": str(self.apikey.key)}
        self.profile = Profile.objects.create(user=self.user)
        response = self.client.get(f"/api/profiles/{self.profile.uuid}", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertNotIsInstance(response.json(), list)

    def test_update_profile(self):
        self.client.force_login(self.user)
        self.profile = Profile.objects.create(user=self.user)
        profile_data = {
            "birth_date": "2024-01-01",
            "bio": "test",
            "skills": "{[1, 2, 3]}",
        }
        response = self.client.put(
            f"/api/profiles/update/{self.profile.uuid}",
            profile_data,
            format="json",
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()["birth_date"], profile_data["birth_date"])
        self.assertEquals(response.json()["bio"], profile_data["bio"])
        self.assertEquals(response.json()["skills"], profile_data["skills"])

    def test_update_profile_unauth(self):
        profile_data = {
            "birth_date": "2024-01-01",
            "bio": "test",
        }
        self.profile = Profile.objects.create(user=self.user)
        response = self.client.put(
            f"/api/profiles/update/{self.profile.uuid}",
            profile_data,
            format="json",
        )
        self.assertEquals(response.status_code, 403)
