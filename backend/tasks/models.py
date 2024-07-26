from django.db import models

from .enums import TaskStatus


class Task(models.Model):
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
        choices=TaskStatus.choices,
        default=TaskStatus.IN_QUEUE,
    )
    create_date = models.DateTimeField(
        'Время создания',
        auto_now_add=True
    )
