from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return render(request, 'posts/index.html')


def group(request, any):
    return HttpResponse("<h1>Группа</h1>")
