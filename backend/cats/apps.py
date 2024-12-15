"""Модуль конфигурации приложения для веб-приложения."""
from django.apps import AppConfig


class CatsConfig(AppConfig):
    """Конфигурация приложения cats."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cats'
