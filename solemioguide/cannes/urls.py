from django.urls import path, re_path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:cat_id>/', views.categories, name='cat_id'),
    path('category/<slug:cat_slug>/', views.categories_by_slug, name='cat_slug'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]