from django.db import models

class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)

    def __str__(self):
      return self.name