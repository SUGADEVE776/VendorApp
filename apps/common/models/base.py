import uuid

from django.db import models

from apps.common.managers import BaseObjectManagerQuerySet

COMMON_CHAR_FIELD_MAX_LENGTH = 512
COMMON_NULLABLE_FIELD_CONFIG = {
    "default": None,
    "null": True,
}
COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG = {
    **COMMON_NULLABLE_FIELD_CONFIG,
    "blank": True,
}


class BaseModel(models.Model):
    """
    Contains the last modified and the created fields, basically
    the base model for the entire app.
    """

    # unique id field
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    # time tracking
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    # custom manager
    objects = BaseObjectManagerQuerySet.as_manager()

    class Meta:
        abstract = True
