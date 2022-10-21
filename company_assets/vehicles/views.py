from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from company_assets.vehicles.models.vehicle import Vehicle
from rest_framework import viewsets

from company_assets.vehicles.serializers import VehicleSerializer

# Create your views here.
class VehicleViewset(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "teacher": ["exact", "gt", "lt"],
        "plate_number": ["exact", "gt", "lt"],
    }
