
from devume.models.country import Country
from django.test import TestCase


class CountryModelTestCase(TestCase):
    def setUp(self):
        return None
    
    def test_country_list(self):
        self.country = Country.objects.create(name='United States', country_code='US')
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(self.country.name, 'United States')