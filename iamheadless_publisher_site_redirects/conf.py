from django.conf import settings as dj_settings

from iamheadless_publisher_site.conf import settings as iamheadless_publisher_site_settings

from .apps import IamheadlessPublisherSiteRedirectsConfig as AppConfig


class Settings:

    APP_NAME = AppConfig.name
    VAR_PREFIX = APP_NAME.upper()

    @property
    def API_CLIENT(self):
        return iamheadless_publisher_site_settings.API_CLIENT

    @property
    def PROJECT_ID(self):
        return iamheadless_publisher_site_settings.PROJECT_ID

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
