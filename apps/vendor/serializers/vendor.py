from apps.common.serializers import (
    AppReadOnlyModelSerializer,
    AppWriteOnlyModelSerializer,
)
from apps.vendor.models import Vendor


class VendorListSerializer(AppReadOnlyModelSerializer):
    """Vendor List Serializer"""

    class Meta(AppReadOnlyModelSerializer.Meta):
        model = Vendor
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "email",
        ]


class VendorCUDSerializer(AppWriteOnlyModelSerializer):
    """Vendor CUD Serializer"""

    class Meta(AppWriteOnlyModelSerializer.Meta):
        model = Vendor
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "address",
        ]


class VendorDetailSerializer(AppReadOnlyModelSerializer):
    """Vendor Detail Serializer"""

    class Meta(AppReadOnlyModelSerializer.Meta):
        model = Vendor
        fields = [
            "id",
            "uuid",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "address",
        ]
