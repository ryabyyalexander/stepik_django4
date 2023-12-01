from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения cannes")


def categories(request, cat_id):
    return HttpResponse(f"<h3>Статьи по категориям</h3><h1>id: {cat_id}</h1>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h3>Статьи по категориям</h3><h1>slug: {cat_slug}</h1>")


def archive(request, year):
    return HttpResponse(f"<h3>Статьи по годам</h3><h1>{year}</h1>")