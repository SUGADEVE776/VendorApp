from apps.common.views import (
    AppModelCUDAPIViewSet,
    AppModelListAPIViewSet,
    AppModelRetrieveAPIViewSet,
)
from apps.vendor.models import Vendor
from apps.vendor.serializers import (
    VendorCUDSerializer,
    VendorDetailSerializer,
    VendorListSerializer,
)


class VendorListAPIViewSet(AppModelListAPIViewSet):
    """Vendor List ViewSet"""

    queryset = Vendor.objects.all()
    serializer_class = VendorListSerializer


class VendorCUDAPIViewSet(AppModelCUDAPIViewSet):
    """Vendor CUD ViewSet"""

    queryset = Vendor.objects.all()
    serializer_class = VendorCUDSerializer


class VendorDetailAPIViewSet(AppModelRetrieveAPIViewSet):
    """Vendor List ViewSet"""

    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
