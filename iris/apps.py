from django.apps import AppConfig
from health_check.plugins import plugin_dir


class IrisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iris'

    def ready(self):
        from iris.backends import IrisTableCheckBackend
        plugin_dir.register(IrisTableCheckBackend)
