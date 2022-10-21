from rest_framework import routers
from company_assets.vehicles.views import VehicleViewset

router = routers.SimpleRouter()
router.register(r"", VehicleViewset)
urlpatterns = router.urls
