from django.db import models

class SiteInfo(models.Model):
    site_name = models.CharField(max_length=255)
    site_adresse = models.CharField(max_length=255)
    copyright = models.CharField(max_length=255)
    site_email = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=6, decimal_places=3)
    latitude = models.DecimalField(max_digits=6, decimal_places=3)