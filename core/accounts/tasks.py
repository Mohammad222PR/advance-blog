from celery import shared_task


@shared_task
def test():
    print('that is test')