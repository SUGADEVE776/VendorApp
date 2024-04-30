from django.contrib.auth.models import User
from rest_framework import serializers

from apps.common.serializers import (
    AppReadOnlyModelSerializer,
    AppWriteOnlyModelSerializer,
)
from apps.vendor.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    """Vendor list cud serializer"""

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Vendor
        fields = ["id", "name", "contact_details", "address", "vendor_code", "user"]


class VendorDetailSerializer(serializers.ModelSerializer):
    """Vendor Detail Serializer"""

    class Meta:
        model = Vendor
        fields = [
            "id",
            "name",
            "contact_details",
            "address",
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
