# TALLER
# COMBUSTIBLE
# LIMPIEZA - CADA SEMANA
from company_assets.vehicles.models.vehicle import Vehicle
from utils.models import BaseModel
from django.db import models


class VehicleRegister(BaseModel):
    total = models.FloatField()
    invoice = models.FileField(upload_to="pdf")

    class Meta:
        abstract = True
