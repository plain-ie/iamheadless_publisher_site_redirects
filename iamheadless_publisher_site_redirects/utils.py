from django.conf import settings as dj_settings

from .conf import settings


def get_client():
    return settings.API_CLIENT
