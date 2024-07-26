from django.db import models


class ApplicationStatus(models.TextChoices):
    """Статусы задач"""
    IN_QUEUE = 'in_queue', 'В очереди'
    PROCESSING = 'processing', 'Выполняется'
    COMPLETED = 'completed', 'Завершена'
