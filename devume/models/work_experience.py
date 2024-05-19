from django.db import models
from .profile import Profile


class WorkExperience(models.Model):
    # id = models.IntegerField(primary_key = True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    skills = models.JSONField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
