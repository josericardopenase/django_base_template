from rest_framework import routers
from .views import ViewSet

router = routers.SimpleRouter()
router.register(r"secretary_profiles", ViewSet)

urlpatterns = router.urls
