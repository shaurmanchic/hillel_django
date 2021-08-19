from django.http import HttpResponse

from django.shortcuts import render

from .models import Exchange

def list_exchange_rates(request):
    exchange_list = Exchange.objects.all()
    return HttpResponse(exchange_list)
