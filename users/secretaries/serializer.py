from rest_framework import serializers
from .models import SecretaryProfile


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = SecretaryProfile
        fields = "__all__"
