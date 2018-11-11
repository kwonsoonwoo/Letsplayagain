from django.db import models


class Kidscafe(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_road = models.CharField(max_length=200, blank=True, null=True)
    tell = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    check_date = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
