from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
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


class POAcknowledgeAPIView(APIView):
    """Acknowledge to PO views"""

    def post(self, request, *args, **kwargs):
        """Handle on post"""

        instance = get_object_or_404(
            PurchaseOrder.objects.all(), id=kwargs.get("po_id")
        )
        instance.acknowledgment_date = timezone.now()
        instance.save()
        instance.calculate_average_response_time()
        return Response(
            {"data": f"Purchase Order {instance.po_number} Acknowledged Successfully"}
        )
