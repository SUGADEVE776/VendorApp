from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg, F

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
    quality_rating = models.FloatField(
        **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    issue_date = models.DateTimeField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    acknowledgment_date = models.DateTimeField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)

    completed_date = models.DateTimeField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    # adding this field for calculating performance metrics

    class Meta(BaseModel.Meta):
        default_related_name = "related_purchase_orders"

    def calculate_ontime_delivery_rate(self):
        """To calculate performance of Vendor"""

        vendor_po_objs = PurchaseOrder.objects.filter(
            vendor=self.vendor, status=PurchaseOrderChoices.completed
        )
        total_po_count = vendor_po_objs.count()
        completed_count = vendor_po_objs.filter(
            completed_date__lte=models.F("delivery_date")
        ).count()
        delivery_rate = (completed_count / total_po_count) * 100
        Performance.objects.update_or_create(
            vendor=self.vendor, defaults={"on_time_delivery_rate": delivery_rate}
        )

    def calculate_quality_rating_average(self):
        """To calculate average quality rating"""

        vendor_po_objs = PurchaseOrder.objects.filter(vendor=self.vendor)
        quality_avg = vendor_po_objs.aggregate(Avg("quality_rating"))[
            "quality_rating__avg"
        ]
        Performance.objects.update_or_create(
            vendor=self.vendor, defaults={"quality_rating_avg": quality_avg}
        )

    def calculate_average_response_time(self):
        """To calculate average response time"""

        vendor_po_objs = PurchaseOrder.objects.filter(vendor=self.vendor)
        average_response_time = (
            vendor_po_objs.annotate(
                response_time=F("acknowledgment_date") - F("issue_date")
            )
            .values_list("response_time", flat=True)
            .aggregate(Avg("response_time"))["response_time__avg"]
            .total_seconds()
        )
        avg_response_hours = (average_response_time % (24 * 3600)) // 3600
        Performance.objects.update_or_create(
            vendor=self.vendor,
            defaults={"average_response_time": avg_response_hours},
        )

    def calculate_fulfillment_rate(self):
        """To calculate fulfillment rate"""

        vendor_po_objs = PurchaseOrder.objects.filter(vendor=self.vendor)
        total_po_count = vendor_po_objs.count()
        completed_count = vendor_po_objs.filter(
            status=PurchaseOrderChoices.completed
        ).count()
        delivery_rate = (completed_count / total_po_count) * 100
        Performance.objects.update_or_create(
            vendor=self.vendor, defaults={"fulfillment_rate": delivery_rate}
        )
