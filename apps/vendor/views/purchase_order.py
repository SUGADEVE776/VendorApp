from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.vendor.models import PurchaseOrder
from apps.vendor.serializers import (
    PurchaseOrderDetailSerializer,
    PurchaseOrderSerializer,
)


class PurchaseOrderModelViewSet(ModelViewSet):
    """Common Purchase Order Operations"""

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def retrieve(self, request, *args, **kwargs):
        """Overridden to add Detail Serializer"""

        instance = self.get_object()
        serializer = PurchaseOrderDetailSerializer(instance)
        return Response(serializer.data)
