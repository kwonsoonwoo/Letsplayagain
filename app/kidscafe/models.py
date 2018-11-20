from django.contrib.gis.db import models


class Kidscafe(models.Model):
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    address_road = models.TextField(blank=True, null=True)
    tell = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    check_date = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
