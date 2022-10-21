from django.db import models


class SecretaryProfile(models.Model):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="secretary_profile"
    )
