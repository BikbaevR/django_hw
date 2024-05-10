from django.apps import AppConfig


class OldAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'old_app'
