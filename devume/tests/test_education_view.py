from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from devume.models.education import Education
from devume.models.profile import Profile
from devume.models.api_key import ApiKey


class EducationViewTestCase(APITestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.profile = Profile.objects.create(user=self.user)
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_education_list_session_auth(self):
        self.client.force_login(self.user)
        self.education = Education.objects.create(profile=self.profile)
        response = self.client.get("/api/education")
        self.assertEqual(len(response.data), 1)

    def test_education_list_api_key_auth(self):
        headers = {"x-api-key": str(self.apikey.key)}
        self.education = Education.objects.create(profile=self.profile)
        response = self.client.get("/api/education", headers=headers)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_education_session_auth(self):
        self.client.force_login(self.user)
        self.education = Education.objects.create(profile=self.profile)
        self.education = Education.objects.create(profile=self.profile)
        response = self.client.get(f"/api/education/{self.profile.uuid}")
        self.assertEqual(len(response.data), 2)

    def test_retrieve_education_api_key_auth(self):
        headers = {"x-api-key": str(self.apikey.key)}
        self.education = Education.objects.create(profile=self.profile)
        self.education = Education.objects.create(profile=self.profile)
        response = self.client.get(
            f"/api/education/{self.profile.uuid}", headers=headers
        )
        self.assertEqual(len(response.data), 2)

    def test_update_education(self):
        self.client.force_login(self.user)
        self.education = Education.objects.create(profile=self.profile)
        education_data = {"degree": "Bachelors", "school_name": "NYU"}
        response = self.client.patch(
            f"/api/education/{self.education.id}/update", education_data
        )
        self.assertEqual(
            response.data["school_name"], education_data["school_name"]
        )
        self.assertEqual(response.data["degree"], education_data["degree"])

    def test_create_education(self):
        self.client.force_login(self.user)
        education_data = {"degree": "Bachelors", "school_name": "NYU"}
        response = self.client.post("/api/education/create", education_data)
        self.assertEqual(response.status_code, 201)
