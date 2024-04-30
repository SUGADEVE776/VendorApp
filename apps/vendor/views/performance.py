from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.vendor.models import Performance, Vendor
from apps.vendor.serializers import PerformanceDetailSerializer


class PerformanceDetailAPIView(views.APIView):
    """Detail ViewSet to get Vendor Performance"""

    def get(self, request, *args, **kwargs):
        """Handle on Get"""

        instance = get_object_or_404(Performance, vendor_id=kwargs.get("vendor_id"))
        serializer = PerformanceDetailSerializer(instance)
        return Response(serializer.data)
