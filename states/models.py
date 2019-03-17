from django.conf import settings
from django.db import models
from django.utils import timezone


class State(models.Model):
    name = models.CharField(max_length=100)
    API = models.DecimalField(max_digits=10,decimal_places=2)
    WaterPh = models.DecimalField(max_digits=10,decimal_places=2)
    HDI = models.DecimalField(max_digits=10,decimal_places=2)
    PerCapitaIncome = models.DecimalField(max_digits=10,decimal_places=2)
    Photo=models.CharField(max_length=500)
    latitude=models.DecimalField(max_digits=10,decimal_places=6)
    longitude=models.DecimalField(max_digits=10,decimal_places=6)

    def __str__(self):
        return self.name