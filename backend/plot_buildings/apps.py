from django.apps import AppConfig


class ForDevelopmentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "for_development"
    verbose_name = "Под застройку"
