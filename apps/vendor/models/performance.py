from django.db import models

from apps.common.models import (
    COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG,
    COMMON_CHAR_FIELD_MAX_LENGTH,
    BaseModel,
)
from apps.vendor.models.vendor import Vendor


class Performance(BaseModel):
    """stores historical data on vendor performance"""

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    quality_rating_avg = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    average_response_time = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    fulfillment_rate = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)

    class Meta(BaseModel.Meta):
        default_related_name = "related_vendor_performance"
