from django.db import models
import uuid
from django.contrib.auth.models import User


class ApiKey(models.Model):
    key = models.CharField(max_length=255, default=uuid.uuid4().hex, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
