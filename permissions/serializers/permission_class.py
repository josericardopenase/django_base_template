from rest_framework.serializers import ModelSerializer
from ..models.permission_class import PermissionClass


class Serializer(ModelSerializer):
    class Meta:
        model = PermissionClass
        fields = "__all__"
