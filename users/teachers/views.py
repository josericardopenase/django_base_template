from django.shortcuts import render
from rest_framework import viewsets
from users.teachers.serializer import Serializer
from .models import TeacherProfile

# Create your views here.
class ViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = TeacherProfile.objects.all()
