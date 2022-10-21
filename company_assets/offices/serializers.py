from rest_framework import serializers

from utils.serializers import Base64ImageField
from .models import Office


class OfficeSerializer(serializers.ModelSerializer):
    thumbnail = Base64ImageField()
    employees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Office
        fields = "__all__"
