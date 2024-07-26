from django.db import models

from .enums import ApplicationStatus


class Application(models.Model):
    name = models.CharField(
        'Название',
        max_length=200
    )
    description = models.TextField(
        'Описание',
        max_length=2000,
    )
    status = models.CharField(
        'Статус',
        max_length=15,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.IN_QUEUE,
    )
    create_date = models.DateTimeField(
        'Время создания',
        auto_now_add=True
    )
