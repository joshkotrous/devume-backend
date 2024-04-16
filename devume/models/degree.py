from django.db import models

class Degree(models.TextChoices):
    ASSOCIATES = 'Associates'
    BACHELORS = 'Bachelors'
    MASTERS = 'Masters'
    DOCTORATE = 'Doctorate'
