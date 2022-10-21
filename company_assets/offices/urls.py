from rest_framework import routers
from company_assets.offices.views import OfficeViewSet

router = routers.SimpleRouter()
router.register(r"", OfficeViewSet)
urlpatterns = router.urls
