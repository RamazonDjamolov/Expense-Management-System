from django.apps import AppConfig


class MoneyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'money'

    def ready(self):
        from .signals import send_upload_notification
