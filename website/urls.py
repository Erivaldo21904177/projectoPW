from importlib.resources import path

from django.shortcuts import render
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='index')
]