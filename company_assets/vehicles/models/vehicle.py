from django.db import models
from utils.models import BaseModel

VEHICLE_TYPE_FUEL = [
    ("GAS", "Gasolina"),
    ("DIE", "Diesel"),
    ("ELE", "Eléctrico"),
    ("HYB", "Hibrído"),
]

VEHICLE_TYPE_CHOICES = [
    ("CICLOMOTOR", "Ciclomotor"),
    ("MOTORBIKE", "Motocicleta"),
    ("TURISMO", "Turismo"),
    ("CAMION", "Camión"),
]

VEHICLE_STATE = [
    ("USING", "Usandose"),
    ("FIXING", "Reparandose"),
    ("STANDING", "En reserva"),
]

# TALLER
# COMBUSTIBLE
# LIMPIEZA - CADA SEMANA
# ACCIDENTES

# Create your models here.
class Vehicle(BaseModel):
    """

    A class that represents a Vehicle Ej. Cars, Motorbykes, etc...

    """

    thumbnail = models.ImageField()

    name = models.CharField(max_length=200)
    plate_number = models.CharField(max_length=200, unique=True)

    vehicle_type = models.CharField(
        choices=VEHICLE_TYPE_CHOICES, max_length=400, blank=True, null=True
    )
    brand = models.CharField(max_length=400, blank=True, null=True)
    model = models.CharField(max_length=400, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    state = models.CharField(choices=VEHICLE_STATE, max_length=200, default="USING")

    bastidor_number = models.CharField(
        max_length=500, unique=True, null=True, blank=True
    )
    purchase_date = models.DateField(blank=True, null=True)
    fuel_type = models.CharField(choices=VEHICLE_TYPE_FUEL, max_length=300)
    itv_date = models.DateField(blank=True, null=True)
    consumption_per_litter = models.FloatField(blank=True, null=True)

    ficha_tecnica = models.FileField(upload_to="pdf", null=True, blank=True)
    permiso_circulacion = models.FileField(upload_to="pdf", null=True, blank=True)
    seguro = models.FileField(upload_to="pdf", null=True, blank=True)

    licences = models.OneToOneField(
        "licences.License", on_delete=models.SET_NULL, null=True, blank=True
    )

    teacher = models.ForeignKey(
        "teachers.TeacherProfile",
        null=True,
        related_name="work_vehicles",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.plate_number
