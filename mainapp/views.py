from django.shortcuts import render
from fish.models import *


def index(request):
    title = 'Главная'
    return render(request, 'index.html', {'page': 'index', 'title': title})


def contact(request):
    title = 'Контакты'
    return render(request, 'contact.html', {'page': 'contact', 'title': title})


def services(request):
    title = 'Услуги'
    cat = Category.objects.all()
    return render(request, 'services.html', {'page': 'services', 'title': title, 'category': cat})


def locks(request):
    title = 'Плетение'
    locks = Locks.objects.all()
    return render(request, 'locks.html', {'locks': locks, 'title': title})


def hairdress(request):
    title = 'Прическа'
    hairdress = Hairdress.objects.all()
    return render(request, 'hairdress.html', {'hairdress': hairdress, 'title': title})


def color(request):
    title = 'Окрашивание'
    colors = Color.objects.all()
    return render(request, 'color.html', {'colors': colors, 'title': title})


def haircut(request):
    title = 'Стрижка'
    haircut = Haircut.objects.all()
    return render(request, 'haircut.html', {'haircut': haircut, 'title': title})


def s_wow(request):
    title = 'Услуги'
    cat = Category.objects.all()
    return render(request, 'wow_slider/service_wow.html', {'page': 's_wow', 'title': title, 'category': cat})
