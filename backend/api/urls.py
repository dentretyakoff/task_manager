from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ApplicationViewSet


API_VERSION = settings.API_VERSION

router = DefaultRouter()
router.register('applications', ApplicationViewSet)

urlpatterns = [
    path(f'{API_VERSION}/', include(router.urls)),
]
