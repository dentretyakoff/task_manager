from rest_framework import serializers

from applications.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    """Сериализатор задач."""
    class Meta:
        model = Application
        fields = ('id', 'name', 'description', 'status', 'create_date')
        read_only_fields = ('status', 'create_date')
