from rest_framework import serializers
from utils.serializers import Base64ImageField, Base64PDFField
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    thumbnail = Base64ImageField()
    permiso_circulacion = Base64PDFField(required=False)
    ficha_tecnica = Base64PDFField(required=False)
    seguro = Base64PDFField(required=False)

    class Meta:
        model = Vehicle
        fields = "__all__"
