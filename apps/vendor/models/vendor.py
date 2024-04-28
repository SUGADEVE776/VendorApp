from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import (
    COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG,
    COMMON_CHAR_FIELD_MAX_LENGTH,
    BaseModel,
)


class Vendor(BaseModel):
    """Base Model for Vendor"""

    user = models.OneToOneField(
        to=User, on_delete=models.RESTRICT, **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG
    )
    name = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)
    contact_details = models.TextField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)
    address = models.TextField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    vendor_code = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)
    on_time_delivery_rate = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    quality_rating_avg = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    average_response_time = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    fulfillment_rate = models.FloatField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)

    class Meta(BaseModel.Meta):
        default_related_name = "related_vendor"
