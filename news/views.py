from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print(request)
    return HttpResponse('Страница новостей')

def news2(request):
    print(request)
    return HttpResponse('Страница новостей №2')