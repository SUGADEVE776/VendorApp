from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.vendor.views import PurchaseOrderModelViewSet, VendorModelViewSet

app_name = "vendor"

BASE_URL = "api"

router = SimpleRouter()

router.register(f"{BASE_URL}/vendors", VendorModelViewSet)

router.register(f"{BASE_URL}/purchase_orders", PurchaseOrderModelViewSet)

urlpatterns = [] + router.urls
