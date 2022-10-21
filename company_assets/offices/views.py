from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from company_assets.offices.models import Office
from .serializers import OfficeSerializer
from rest_framework import viewsets

# Create your views here.
class OfficeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {"email": ["exact", "contains"], "name": ["exact", "contains"]}
