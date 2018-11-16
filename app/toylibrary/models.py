from django.db import models


class Toylibrary(models.Model):
    name = models.TextField(blank=True, null=True)
    gu = models.TextField(blank=True, null=True)
    tell = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    address_road = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
