from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'
   #imports signals to ensure they are registered
    def ready(self):
        import properties.signals
