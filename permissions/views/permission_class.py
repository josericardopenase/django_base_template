from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from permissions.models.permission_class import PermissionClass
from permissions.serializers.permission_class import Serializer
from rest_framework import viewsets


class ViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = PermissionClass.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(permission=self.kwargs["permission_id"])
