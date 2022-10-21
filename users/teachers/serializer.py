from rest_framework import serializers
from .models import TeacherProfile


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = "__all__"
