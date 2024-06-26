from rest_framework import serializers

from apps.common.serializers import BaseIDNameSerializer
from apps.vendor.models import Performance


class PerformanceDetailSerializer(serializers.ModelSerializer):
    """Performance Detail Serializer"""

    vendor = BaseIDNameSerializer()

    class Meta:
        model = Performance
        fields = [
            "id",
            "vendor",
            "date",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
