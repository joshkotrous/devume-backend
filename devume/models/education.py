from django.db import models
from .profile import Profile
from .degree import Degree


class Education(models.Model):
    # id = models.IntegerField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=50, choices=Degree.choices, null=True)
    field_of_study = models.CharField(max_length=200, null=True, blank=True, default="")
