from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask


@shared_task
def sendEmail():
    sleep(3)
    print("done sending email dud")


@shared_task
def clean_up_ended_task():
    disable_task = PeriodicTask.objects.filter(enabled=False)
    for task in disable_task:
        task.delete()
        print("Disabling task deleted")
