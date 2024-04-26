from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.common.config import CUSTOM_ERRORS_MESSAGES


class CustomErrorMessagesMixin:
    """
    Overrides the constructor of the serializer to add meaningful error
    messages to the serializer output. Also used to hide security
    related messages to the user.
    """

    def get_display(self, field_name):
        return field_name.replace("_", " ")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding custom error messages
        for field_name, field in getattr(self, "fields", {}).items():
            if field.__class__.__name__ == "ManyRelatedField":
                # many-to-many | uses foreign key field for children
                field.error_messages.update(CUSTOM_ERRORS_MESSAGES["ManyRelatedField"])
                field.child_relation.error_messages.update(
                    CUSTOM_ERRORS_MESSAGES["PrimaryKeyRelatedField"]
                )
            elif field.__class__.__name__ == "PrimaryKeyRelatedField":
                # foreign-key
                field.error_messages.update(
                    CUSTOM_ERRORS_MESSAGES["PrimaryKeyRelatedField"]
                )
            else:
                # other input-fields
                field.error_messages.update(
                    {
                        "blank": f"Please enter your {self.get_display(field_name)}",
                        "null": f"Please enter your {self.get_display(field_name)}",
                    }
                )


class AppSerializer(CustomErrorMessagesMixin, Serializer):
    """
    The app's version for the Serializer class. Just to implement common and
    other verifications and schema. Used only for light weight stuff.
    """

    def get_user(self):
        """Return the user from the request."""

        return self.get_request().user

    def get_request(self):
        """Returns the request."""

        return self.context.get("request", None)


class AppModelSerializer(AppSerializer, ModelSerializer):
    """
    Applications version of the ModelSerializer. There are separate serializers
    defined for handling the read and write operations separately.

    Note:
        Never mix the `read` and `write` serializers, handle them separate.
    """

    class Meta:
        pass


class AppReadOnlyModelSerializer(AppModelSerializer):
    """
    Read only version of the `AppModelSerializer`. Does not
    support write operations.

    Note:
        Never mix the `read` and `write` serializers, handle them separate.
    """

    class Meta(AppModelSerializer.Meta):
        pass

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class AppWriteOnlyModelSerializer(AppModelSerializer):
    """
    Write only version of the `AppModelSerializer`. Does not support read
    operations and to_representations. Validations are implemented here.

    Note:
        Never mix the `read` and `write` serializers, handle them separate.
    """

    class Meta(AppModelSerializer.Meta):
        model = None
        fields = []
        extra_kwargs = {}


class BaseIDNameSerializer(serializers.Serializer):
    """Base serializer for id and name"""

    id = serializers.IntegerField()
    name = serializers.CharField()
