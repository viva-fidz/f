from django.shortcuts import render
from fish.models import *
from mainapp.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


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


def contacts(request):
    title = 'Контакты'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые   пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipient_list = ['viva.fidz@yandex.ru']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recipient_list.append(sender)
            try:
                send_mail(subject, message, 'viva.fidz@yandex.ru',  recipient_list)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
                # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'contacts/thanks.html')
    else:
        # Заполняем форму
        form = ContactForm()
        # Отправляем форму на страницу
    return render(request, 'contacts.html', {'title': title, 'form': form})


def s_wow(request):
    title = 'Услуги'
    cat = Category.objects.all()
    return render(request, 'wow_slider/service_wow.html', {'page': 's_wow', 'title': title, 'category': cat})
