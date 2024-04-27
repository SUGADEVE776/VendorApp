from rest_framework.viewsets import GenericViewSet, mixins

from apps.vendor.models import Performance
from apps.vendor.serializers import PerformanceDetailSerializer


class PerformanceDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """Detail ViewSet to get Vendor Performance"""

    queryset = Performance.objects.all()
    serializer_class = PerformanceDetailSerializer
