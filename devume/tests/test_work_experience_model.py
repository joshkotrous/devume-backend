from devume.models.work_experience import WorkExperience
from django.test import TestCase
from django.contrib.auth.models import User
from devume.models.profile import Profile


class WorkExperienceModelTestCase(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.profile = Profile.objects.create(user=self.user)

    def test_work_experience_creation(self):
        self.work_experience = WorkExperience.objects.create(
            profile=self.profile
        )
        self.assertEqual(WorkExperience.objects.count(), 1)
