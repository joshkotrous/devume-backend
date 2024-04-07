from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testUser', email='testUser@gmail.com', password='testPassword')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.username, 'testUser')
        self.assertEqual(self.user.email, 'testUser@gmail.com')
        self.assertTrue(self.user.check_password('testPassword'))

    def test_user_authentication(self):
        user = User.objects.get(username='testUser')
        self.assertTrue(user.check_password('testPassword'))