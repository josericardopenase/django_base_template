# Django
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers
from .views import permission_class, permission
import re


router = routers.SimpleRouter()
router.register(r"(?P<permission_id>\d+)/classes", permission_class.ViewSet)
router.register(r"", permission.ViewSet)

urlpatterns = router.urls
