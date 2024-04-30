from rest_framework import serializers
from rest_framework.authtoken.models import Token

from apps.vendor.models import PurchaseOrder, Vendor


class PurchaseOrderSerializer(serializers.ModelSerializer):
    """PurchaseOrder CUD Serializer"""

    acknowledgment_date = serializers.DateTimeField(required=False, allow_null=True)
    issue_date = serializers.DateTimeField(required=False)
    completed_date = serializers.DateTimeField(required=False, allow_null=True)
    quality_rating = serializers.FloatField(required=False, allow_null=True)
    vendor = serializers.PrimaryKeyRelatedField(
        queryset=Vendor.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = PurchaseOrder
        fields = [
            "id",
            "po_number",
            "vendor",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "acknowledgment_date",
            "issue_date",
            "completed_date",
            "quality_rating",
        ]


class PurchaseOrderDetailSerializer(serializers.ModelSerializer):
    """PurchaseOrder Detail Serializer"""

    class Meta:
        model = PurchaseOrder
        fields = [
            "id",
            "po_number",
            "vendor",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "issue_date",
            "acknowledgment_date",
        ]
