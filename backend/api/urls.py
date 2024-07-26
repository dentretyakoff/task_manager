from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet


# Версия API
API_VERSION = settings.API_VERSION

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path(f'{API_VERSION}/', include(router.urls)),
]
