from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.vendor.views import (
    PerformanceDetailAPIView,
    POAcknowledgeAPIView,
    PurchaseOrderModelViewSet,
    VendorModelViewSet,
)

app_name = "vendor"

BASE_URL = "api"

router = SimpleRouter()

router.register(f"{BASE_URL}/vendors", VendorModelViewSet)

router.register(f"{BASE_URL}/purchase_orders", PurchaseOrderModelViewSet)


urlpatterns = [
    path(
        f"{BASE_URL}/purchase_orders/<int:po_id>/acknowledge/",
        POAcknowledgeAPIView.as_view(),
    ),
    path(
        f"{BASE_URL}/vendors/<int:vendor_id>/performance/",
        PerformanceDetailAPIView.as_view(),
    ),
] + router.urls
