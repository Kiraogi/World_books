from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Словарь для передачи данных в шаблон
    text_head = "Это заголовок главной страницы"
    text_body = "Это содержимое главной страницы сайта"
    context = {'text_head': text_head, 'text_body': text_body}
    # Передача словоря context с данными в шаблоне
    return render(request, 'catalog/index.html', context)
