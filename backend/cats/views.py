"""Модуль определения представлений для веб-приложения."""
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Achievement, Cat
from .serializers import AchievementSerializer, CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """Представление для работы с объектами Cat."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        """Переопределение сохранения с присвоением владельца."""
        serializer.save(owner=self.request.user)


class AchievementViewSet(viewsets.ModelViewSet):
    """Представление для работы с объектами Achievement."""

    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None
