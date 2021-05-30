from django.apps import AppConfig


class DataCollectionsConfig(AppConfig):
    name = 'data_collections'

    def ready(self):
        from data_collections.signals import handlers  # noqa
