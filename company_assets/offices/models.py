from utils.models import BaseModel
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Office(BaseModel):
    thumbnail = models.ImageField(blank=True)
    name = models.CharField(max_length=200)
    ubication = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField()
