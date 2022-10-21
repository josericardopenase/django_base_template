from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from permissions.models.permission import Permission
from permissions.serializers.permission import Serializer
from rest_framework import viewsets


class ViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = Permission.objects.all()
