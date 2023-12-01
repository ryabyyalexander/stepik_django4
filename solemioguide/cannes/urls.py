from django.urls import path, re_path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index),
    path('category/<int:cat_id>/', views.categories),
    path('category/<slug:cat_slug>/', views.categories_by_slug),
    path('archive/<year4:year>/', views.archive),
]