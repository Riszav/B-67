from celery import shared_task


@shared_task
def add(x, y):
    from time import sleep

    sleep(15)
    print(f"args {x} and {y}")
    return x + y
