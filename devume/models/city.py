from django.db import models
from .state import State
from .country import Country


class City(models.Model):
    # id = models.IntegerField(primary_key=True, default=int)

    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

