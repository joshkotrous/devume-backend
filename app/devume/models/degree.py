from django.db import models

class Degree(models.TextChoices):
    ASSOCIATES = 'A', 'Associates'
    BACHELORS = 'B', 'Bachelors'
    MASTERS = 'M', 'Masters'
    DOCTORATE = 'D', 'Doctorate'
