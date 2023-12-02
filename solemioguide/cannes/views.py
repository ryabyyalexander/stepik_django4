from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse


menu = ['main', 'about', 'contact']
def index(request):
    # t = render_to_string('cannes/index.html')
    # return HttpResponse(t)
    data = {'title': 'Главная страница?',
            'menu': menu}
    return render(request, 'cannes/index.html', context=data)

def about(request):
    return render(request, 'cannes/about.html', {'title': 'О сайте'})
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
        uri = reverse('archive', args=(2023, )) # вычисляем путь url
        return redirect(uri) # ошибка 302
    return HttpResponse(f"<h3>Статьи по годам</h3><h1>{year}</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")