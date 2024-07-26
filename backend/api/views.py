from rest_framework import viewsets

from applications.models import Application
from applications.tasks import process_application

from .serializers import ApplicationSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """Вьюсет задач, выполянет все операции CRUD."""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        application = serializer.save()
        process_application.delay(application.id)
