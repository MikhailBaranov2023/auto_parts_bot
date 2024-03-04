import uuid
from asgiref.sync import sync_to_async
from yookassa import Configuration, Payment

Configuration.account_id = "334417"
Configuration.secret_key = "test_aUfavu_fgLcP03c-Xl84o08R0J3Iqzj66N-cQUgRgL8"


@sync_to_async
def create_payment():
    payment = Payment.create({
        "amount": {
            "value": "1000.00",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://www.example.com/return_url"
        },
        "capture": True,
        "description": "единоразовая оплата"
    }, uuid.uuid4())
    payment_id = payment.id
    confirmation_url = payment.confirmation.confirmation_url
    return confirmation_url, payment_id


@sync_to_async
def check_status_payment(payment_id):
    while True:
        payment = Payment.find_one(payment_id)
        if payment.status == 'succeeded' or payment.status == 'waiting_for_capture':
            return True
        elif payment.status == 'canceled':
            return False
        continue
