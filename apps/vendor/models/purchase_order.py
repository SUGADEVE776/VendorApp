from django.db import models
from django.db.models import Avg

from apps.common.models import (
    COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG,
    COMMON_CHAR_FIELD_MAX_LENGTH,
    BaseModel,
)
from apps.vendor.config import PurchaseOrderChoices
from apps.vendor.models.performance import Performance
from apps.vendor.models.vendor import Vendor


class PurchaseOrder(BaseModel):
    """Details of each purchase order"""

    po_number = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH, unique=True)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG
    )
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(
        choices=PurchaseOrderChoices.choices, max_length=COMMON_CHAR_FIELD_MAX_LENGTH
    )
    quality_rating = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    issue_date = models.DateTimeField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    acknowledgment_date = models.DateTimeField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)

    completed_date = models.DateTimeField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    # adding this field for calculating performance metrics

    class Meta(BaseModel.Meta):
        default_related_name = "related_purchase_orders"

    def calculate_ontime_delivery_rate(self):
        """To calculate performance of Vendor"""

        vendor_po_objs = PurchaseOrder.objects.filter(vendor=self.vendor)
        total_po_count = vendor_po_objs.count()
        completed_count = vendor_po_objs.filter(
            status=PurchaseOrderChoices.completed, delivery_date__lte=completed_date
        ).count()
        delivery_rate = completed_count // vendor_po_objs
        Performance.objects.update_or_create(
            vendor=self.vendor, defaults={"on_time_delivery_rate": delivery_rate}
        )

    def calculate_quality_rating_average(self):
        """To calculate average quality rating"""

        vendor_po_objs = PurchaseOrder.objects.filter(vendor=self.vendor)
        quality_avg = vendor_po_objs.aggregate(Avg("quality_rating"))
        Performance.objects.update_or_create(
            vendor=self.vendor, defaults={"quality_rating_avg": quality_avg}
        )

    def calculate_average_response_time(self):
        """To calculate average response time"""

        vendor_po_objs = PurchaseOrder.objects.filter(vendor=self.vendor)
        pass

    def calculate_fulfillment_rate(self):
        """To calculate fulfillment rate"""
        pass
