from django.db import models


class Culture(models.Model):
    gu = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.CharField(max_length=255, blank=True)
    end_date = models.CharField(max_length=255, blank=True)
    time = models.CharField(max_length=255, blank=True)
    homepage = models.URLField()
    target_user = models.CharField(max_length=255, blank=True, null=True)
    fee = models.CharField(max_length=255, blank=True, null=True)
    inquiry = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.place
