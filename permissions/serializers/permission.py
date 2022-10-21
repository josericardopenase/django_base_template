from rest_framework.serializers import ModelSerializer
from ..models.permission import Permission


class Serializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
