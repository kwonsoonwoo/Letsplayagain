from django.db import models


class Culture(models.Model):
    gu = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    start_date = models.TextField(blank=True)
    end_date = models.TextField(blank=True)
    time = models.TextField(blank=True)
    homepage = models.TextField(blank=True, null=True)
    target_user = models.TextField(blank=True, null=True)
    fee = models.TextField(blank=True, null=True)
    inquiry = models.TextField(blank=True, null=True)
    program = models.TextField(blank=True, null=True)
    contents = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.place
