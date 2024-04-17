from devume.models.city import City
from django.test import TestCase
from devume.models.state import State
from devume.models.country import Country


class CityModelTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="United States", country_code="US")
        self.state = State.objects.create(name="New York", country_id=self.country.id)

    def test_city_creation(self):
        self.city = City.objects.create(name="New York City", state_id=self.state.id)
        self.assertEqual(City.objects.count(), 1)
        self.assertEqual(self.city.name, "New York City")
