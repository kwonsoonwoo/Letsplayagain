from django.db import models


class Toylibrary(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    gu = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address_road = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
