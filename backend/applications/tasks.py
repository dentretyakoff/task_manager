import time

from celery import shared_task

from exceptions.apps import ApplicationNotFoundError
from .enums import ApplicationStatus
from .models import Application


@shared_task
def process_application(application_id):
    try:
        application = Application.objects.get(pk=application_id)
        application.status = ApplicationStatus.PROCESSING
        application.save()

        time.sleep(15)

        application.status = ApplicationStatus.COMPLETED
        application.save()
    except Application.DoesNotExist:
        raise ApplicationNotFoundError(
            f'Заявка с id = {application_id} не найдена.')
