from celery import shared_task
from advert.models import Car, Request, Request_To_Repair


@shared_task
def get_requests():
    pass
