from devume.models.state import State
from django.test import TestCase
from devume.models.country import Country


class StateModelTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="United States", country_code="US")

    def test_states_create(self):
        self.state = State.objects.create(name='New York', state_code='NY',country_id=self.country.id)
        self.assertEqual(State.objects.count(), 1)
        self.assertEqual(self.state.name, 'New York')
