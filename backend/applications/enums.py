from django.db import models


class ApplicationStatus(models.TextChoices):
    """Статусы заявок."""
    IN_QUEUE = 'in_queue', 'В очереди'
    PROCESSING = 'processing', 'Выполняется'
    COMPLETED = 'completed', 'Завершена'
