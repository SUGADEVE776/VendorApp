from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.vendor.views import (
    VendorCUDAPIViewSet,
    VendorDetailAPIViewSet,
    VendorListAPIViewSet,
)

app_name = "vendor"

BASE_URL = "api"

router = SimpleRouter()

router.register(f"{BASE_URL}/vendors/cud", VendorCUDAPIViewSet)
router.register(f"{BASE_URL}/vendors/list", VendorListAPIViewSet)
router.register(f"{BASE_URL}/vendors/detail", VendorDetailAPIViewSet)


urlpatterns = [] + router.urls
