from django.db import models
from .country import Country


class State(models.Model):
    # id = models.IntegerField(primary_key=True, default=int)

    name = models.CharField(max_length=50)
    state_code = models.CharField(max_length=2)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
