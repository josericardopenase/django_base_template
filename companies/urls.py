from rest_framework import routers
from .views import ViewSet

router = routers.SimpleRouter()
router.register(r"", ViewSet)

urlpatterns = router.urls
