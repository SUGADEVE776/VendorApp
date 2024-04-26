from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.status import is_success


class NonAuthenticatedAPIMixin:
    """
    The mixin class which defines an API class as non-authenticated.
    The users can access this api without login. Just DRY stuff.
    """

    permission_classes = [permissions.AllowAny]


class AppViewMixin:
    """
    The base view class for all the application view. Contains common methods
    and overrides to main integrity and schema.
    """

    def get_request(self):
        """Returns the request."""

        return self.request

    def get_user(self):
        """Returns the current user."""

        return self.get_request().user

    def get_authenticated_user(self):
        """Returns the authenticated user."""

        user = self.get_user()
        return user if user and user.is_authenticated else None

    def send_error_response(self, data=None):
        """Central function to send error response."""

        return self.send_response(data=data, status_code=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def send_response(
        data=None,
        status_code=status.HTTP_200_OK,
        action_code="DO_NOTHING",
        **other_response_data
    ):
        """Custom function to send the centralized response."""

        return Response(
            data={
                "data": data,
                "status": "success" if is_success(status_code) else "error",
                "action_code": action_code,
                **other_response_data,
            },
            status=status_code,
        )


class LoggedInUserMixin:
    """To filter based on Logged in User"""

    def get_queryset(self):
        """Overridden to get queryset based on logged-in user"""

        return super().get_queryset().filter(user=self.get_user())
