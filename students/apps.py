from django.apps import AppConfig


class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'

    def ready(self):
        from .handlers import phone_edit_handler
