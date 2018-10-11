from django.db import models


class Toylibrary(models.Model):
    name = models.CharField(max_length=255)
    gu = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_road = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
