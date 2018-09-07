from rest_framework import permissions
from service_area.models import AccessToken
import datetime
from django.core.exceptions import ValidationError
from service_area.constants import ACCESS_TOKEN_EXPIRY


def get_token(request):
    """
    This method is used to get token from request meta tag
    :param request:
    :return:
    """
    try:
        token = request.META["HTTP_AUTHORIZATION"].split(' ')[1]
        return AccessToken.objects.\
            get(token=token, expiry__gte=datetime.datetime.now(), is_deleted=False)

    except (KeyError, IndexError, AccessToken.DoesNotExist, ValidationError):
        return None


class CompanyAccessPermission(permissions.BasePermission):
    """
    User permission to check if user is allowed to access Customer Dashboard.
    """

    def has_permission(self, request, view):
        token = get_token(request)
        if token and not token.company.is_deleted:
            request.user = token.company
            token.expiry += datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRY)
            token.save()
            return True
        else:
            return False
