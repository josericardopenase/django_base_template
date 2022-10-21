from django.db import models

CHOICES = [
    ("AM", "AM"),
    ("A1", "A1"),
    ("A2", "A2"),
    ("A", "A"),
    ("B", "B"),
]

# Create your models here.
class Permission(models.Model):
    name = models.CharField(max_length=255)
    dgt_name = models.CharField(max_length=255, choices=CHOICES)
