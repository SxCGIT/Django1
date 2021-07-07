from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = 'conduit.api.users'
    verbose_name = _("Api_User")

    def ready(self):
        try:
            import conduit.api.users.signals  # noqa F401
        except ImportError:
            pass