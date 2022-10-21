from django.db import models

from utils.models import ScheduleModel


class TeacherProfile(ScheduleModel):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="teacher_profile"
    )
