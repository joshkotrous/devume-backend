from django.contrib.auth.models import User
from django.db import models
import uuid

from .city import City
from .state import State
from .country import Country

# Create your models here.
class Profile(models.Model):

    uuid = models.UUIDField(primary_key = True, default=uuid.uuid4)
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=1000, null=True, blank=True )
    city = models.ForeignKey(City,  on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
      return self.name