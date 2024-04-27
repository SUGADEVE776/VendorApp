from django.db import models

from apps.common.models import (
    COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG,
    COMMON_CHAR_FIELD_MAX_LENGTH,
    BaseModel,
)
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
    status = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)
    quality_rating = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    issue_date = models.DateTimeField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    acknowledgment_date = models.DateTimeField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)

    class Meta(BaseModel.Meta):
        default_related_name = "related_purchase_orders"
