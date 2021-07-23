from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import News

def index(request):
    news = News.objects.all()
    res = '<h1>Список новостей<h1>'
    for item in news:
        res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    #print(request)
    return HttpResponse(res)

def news2(request):
    print(request)
    return HttpResponse('Страница новостей №2')