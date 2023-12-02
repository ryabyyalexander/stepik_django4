from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect


def index(request):
    return HttpResponse("<h1>Страница приложения cannes</h1>")


def categories(request, cat_id):
    return HttpResponse(f"<h3>Статьи по категориям</h3><h1>id: {cat_id}</h1>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h3>Статьи по категориям</h3><h1>slug: {cat_slug}</h1>")


def archive(request, year):
    if year > 2023:
        # raise Http404() # вызов функции page_not_found
        # return redirect('/', permanent=True) # ошибка 301 перенапрвление на постоянный адрес
        return redirect('cat_id', '10')
    return HttpResponse(f"<h3>Статьи по годам</h3><h1>{year}</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")