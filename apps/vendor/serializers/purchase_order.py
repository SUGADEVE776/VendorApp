from rest_framework import serializers

from apps.vendor.models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    """PurchaseOrder CUD Serializer"""

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
