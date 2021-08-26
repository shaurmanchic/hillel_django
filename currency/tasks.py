import requests
from celery import shared_task

from .models import Exchange
from .choices import CURRENCIES


@shared_task
def get_currency_rates():
    exhange_response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    while True:
        exchange_result = exhange_response.json()
        for rate in exchange_result:
            if rate.get('ccy') not in [currency[0] for currency in CURRENCIES]:
                continue

            exchange = Exchange(
                currency=rate.get('ccy', 'USD'),
                buy_price=rate.get('buy'),
                sell_price=rate.get('sale')
            )
            exchange.save()
        
        return 'All saved successfully'


# python manage.py runserver & \
#     celery -A hillel_django_project worker -l info --concurrency 1 -P solo & \
#     celery -A hillel_django_project beat -l info

# celery -A hillel_django_project worker -l info --concurrency 1 -P solo