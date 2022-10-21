from rest_framework import viewsets
from users.secretaries.serializer import Serializer
from .models import SecretaryProfile

# Create your views here.
class ViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = SecretaryProfile.objects.all()
