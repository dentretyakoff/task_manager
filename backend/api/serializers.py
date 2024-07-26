from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор задач."""
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status', 'create_date')
        read_only_fields = ('status', 'create_date')
