from rest_framework import viewsets

from tasks.models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Вьюсет задач, выполянет все операции CRUD."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
