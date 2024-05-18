from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.


class Profile(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    skills = models.JSONField(null=True, blank=True, default=dict)
    link_1 = models.CharField(max_length=2000, blank=True, null=True)
    link_2 = models.CharField(max_length=2000, blank=True, null=True)
    link_3 = models.CharField(max_length=2000, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)

    # def __str__(self):
    #     return self.name
