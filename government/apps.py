from django.apps import AppConfig


class GovernmentConfig(AppConfig):
    name = 'government'

    def ready(self):
        from government import signals  # noqa
