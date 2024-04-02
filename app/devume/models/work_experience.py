from django.db import models
from .profile import Profile

class WorkExperience(models.Model):
    id = models.IntegerField(primary_key = True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    skills = models.JSONField()
    start_date = models.DateField()
    end_date = models.DateField()


    