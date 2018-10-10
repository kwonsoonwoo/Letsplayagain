from django.db import models


class Toylibrary(models.Model):
    name = models.CharField(max_length=255)
    gu = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_road = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=25, decimal_places=25)
    longitude = models.DecimalField(max_digits=25, decimal_places=25)
