from django.http import HttpResponse
from django.shortcuts import render

from attributes.models import Categories


def index(request):


    context = {
        'title': 'BASKET-SHOP - Главная',
        'content': "Баскетбольный магазин",
    }

    return render(request, 'app/index.html', context)


def about(request):
    context = {
        'title': 'BASKET-SHOP - О нас',
        'content': "О нас",
        
    }

    return render(request, 'app/about.html', context)


def dostavca(request):
    context = {
        'title': 'BASKET-SHOP - Доставка и оплата',
        'content': "Доставка и оплата",
        
    }

    return render(request, 'app/dostavca.html', context)


def contact(request):
    context = {
        'title': 'BASKET-SHOP - Контакты',
        'content': "Контакты",
    }

    return render(request, 'app/contact.html', context)

