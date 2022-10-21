from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from users.serializer import (
    UserSerializer,
)
from companies.serializer import Serializer as CompanySerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(company=self.request.user.company)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def Me(request):
    serializer = UserSerializer(request.user, context={"request": request})
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def MeCompany(request):
    serializer = CompanySerializer(request.user.company, context={"request": request})
    return Response(serializer.data)
