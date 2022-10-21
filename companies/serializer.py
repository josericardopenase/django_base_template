from rest_framework import serializers
from .models import Company


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
