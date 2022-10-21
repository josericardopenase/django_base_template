# Django
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers
from users.views import (
    MeCompany,
    UserViewSet,
    Me,
)

router = routers.SimpleRouter()
router.register(r"", UserViewSet)

urlpatterns = [
    path("secretary_profiles/", include("users.secretaries.urls")),
    path("teacher_profiles/", include("users.teachers.urls")),
    path("auth/", views.obtain_auth_token),
    path("me/", Me),
    path("me/company/", MeCompany),
] + router.urls
