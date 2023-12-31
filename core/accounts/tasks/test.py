from celery import shared_task


@shared_task
def Task():
    print("Task completed successfully")

