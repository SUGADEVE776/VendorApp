from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.vendor.views import VendorModelViewSet

app_name = "vendor"

BASE_URL = "api"

router = SimpleRouter()

router.register(f"{BASE_URL}/vendors", VendorModelViewSet)

urlpatterns = [] + router.urls
