from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Главная страница тестового проекта')

def group_posts(request, slug):
    return HttpResponse(f'Привет, я страница группы или что-то такое {slug}')
    pass