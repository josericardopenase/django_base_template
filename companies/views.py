from rest_framework import viewsets
from .serializer import Serializer
from .models import Company

# Create your views here.
class ViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = Company.objects.all()
