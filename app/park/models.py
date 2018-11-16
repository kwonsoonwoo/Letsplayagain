from django.db import models


class Park(models.Model):
    name = models.TextField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    use_note = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    tell = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
