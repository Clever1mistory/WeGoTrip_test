from celery import shared_task
import requests


@shared_task
def send_webhook_request(order_id, amount, confirmation_time):
    webhook_url = 'https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4'

    data = {
        'id': order_id,
        'amount': amount,
        'date': confirmation_time,
    }
    response = requests.post(webhook_url, json=data)
    print(response.json())
