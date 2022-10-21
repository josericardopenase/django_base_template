from django.db import models


# Create your models here.
class License(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=20, null=True, blank=True)
