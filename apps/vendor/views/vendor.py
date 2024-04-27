from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.common.views import (
    AppModelCUDAPIViewSet,
    AppModelListAPIViewSet,
    AppModelRetrieveAPIViewSet,
)
from apps.vendor.models import Vendor
from apps.vendor.serializers import VendorDetailSerializer, VendorSerializer


class VendorModelViewSet(ModelViewSet):
    """Vendor List ViewSet"""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def create(self, request, *args, **kwargs):
        """Overridden to create a user"""

        data = request.data
        email = data.pop("email")
        user, _ = User.objects.get_or_create(
            email=email, defaults={"first_name": data.get("name")}
        )
        user.set_password(email)
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Overridden to add detail serializer"""

        instance = self.get_object()
        serializer = VendorDetailSerializer(instance)
        return Response(serializer.data)
