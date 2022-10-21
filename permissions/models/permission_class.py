from django.db import models


class PermissionClass(models.Model):
    permission = models.ForeignKey("permissions.Permission", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    duration = models.IntegerField()
