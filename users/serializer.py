from rest_framework import serializers
from users.models import User
from utils.serializers import Base64ImageField
from company_assets.offices.models import Office


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    company = serializers.PrimaryKeyRelatedField(read_only=True)
    avatar = Base64ImageField(required=False, allow_null=True)
    secretary_profile = serializers.PrimaryKeyRelatedField(read_only=True)
    teacher_profile = serializers.PrimaryKeyRelatedField(read_only=True)
    offices = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Office.objects.all(), required=False
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "role",
            "avatar",
            "company",
            "has_holded_profile",
            "secretary_profile",
            "teacher_profile",
            "offices",
            "phone_number",
            "address",
            "postal_code",
            "city",
            "province",
        ]

    def create(self, validated_data):
        company = self.context["request"].user.company
        user = User.objects.create(  # this line  will solve your problem
            **validated_data,
            company=company,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
