from django.apps import AppConfig


class AppAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_admin'
    # Название в панели управления
    verbose_name = 'Панель управления'