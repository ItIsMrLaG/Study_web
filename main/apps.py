# >>>файл для прописывания глобальных настроек для данного приложения<<<
from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
