from django.db import models

from apps.common.models import (
    COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG,
    COMMON_CHAR_FIELD_MAX_LENGTH,
    BaseModel,
)


class Vendor(BaseModel):
    """Base Model for Vendor"""

    first_name = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)
    last_name = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)
    phone_number = models.PhoneNumberField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)
    email = models.EmailField(unique=True)
    address = models.TextField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)

    class Meta(BaseModel.Meta):
        default_related_name = "related_vendor"
