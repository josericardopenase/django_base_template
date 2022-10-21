# Django
from django.urls import path, include
from .views import dgt

urlpatterns = [path("dgt/", dgt)]
