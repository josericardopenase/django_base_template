# Django
from django.urls import path, include

urlpatterns = [
    path("vehicles/", include("company_assets.vehicles.urls")),
    path("offices/", include("company_assets.offices.urls")),
    path("companies/", include("companies.urls")),
    path("users/", include("users.urls")),
    path("metrics/", include("metrics.urls")),
    path("permissions/", include("permissions.urls")),
]
