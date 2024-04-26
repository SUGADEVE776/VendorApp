from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from apps.common.pagination import AppPagination
from apps.common.views.base import AppViewMixin


class AppModelListAPIViewSet(
    AppViewMixin,
    ListModelMixin,
    GenericViewSet,
):
    """
    Applications base list APIViewSet. Handles all the listing views.
    This also sends the necessary filter meta and table config data.

    Also handles listing operations like sort, search, filter
    """

    pagination_class = AppPagination  # page-size: 25
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = []  # override
    search_fields = []  # override
    ordering_fields = "__all__"

    all_table_columns = {}


class AppModelCUDAPIViewSet(
    AppViewMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """
    Urls Allowed:
        > POST: {endpoint}/
            >> Get data from front-end and creates an object.
        > GET: {endpoint}/meta/
            >> Returns metadata for the front-end for object creation.

        > PUT: {endpoint}/<pk>/
            >> Get data from font-end to update an object.
        > GET: {endpoint}/<pk>/meta/
            >> Returns metadata for the front-end for object update.

        > DELETE: {endpoint}/<pk>/
            >> Deletes the object identified by the passed `pk`.
    """


class AppModelRetrieveAPIViewSet(AppViewMixin, RetrieveModelMixin, GenericViewSet):
    """Handle all details of a single objects"""
