from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from devume.models.country import Country
from devume.models.api_key import ApiKey


class CountriesViewTestCase(APITestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.country = Country.objects.create(
            name="United States", country_code="US"
        )
        self.apikey = ApiKey.objects.create(user=self.user)

    def test_get_countries_api_key_auth(self):
        headers = {"x-api-key": str(self.apikey.key)}
        response = self.client.get("/api/countries", headers=headers)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_countries_session_auth(self):
        self.client.force_login(self.user)
        response = self.client.get("/api/countries")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_create_country(self):
        headers = {"x-api-key": str(self.apikey.key)}
        country_data = {"name": "United Kingdom", "country_code": "UK"}
        response = self.client.post(
            "/api/countries/create",
            country_data,
            format="json",
            headers=headers,
        )
        self.assertEqual(response.status_code, 201)

    def test_update_country(self):
        headers = {"x-api-key": str(self.apikey.key)}
        country_data = {"name": "United Kingdom", "country_code": "UK"}
        response = self.client.patch(
            f"/api/countries/{self.country.id}/update",
            country_data,
            format="json",
            headers=headers,
        )
        self.assertEqual(response.status_code, 200)
