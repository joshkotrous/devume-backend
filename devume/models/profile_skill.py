from django.db import models
from .profile import Profile
from devume.models.skill import Skill

class Profile_Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    profile = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,  on_delete=models.CASCADE)

    def __str__(self):
      return self.name