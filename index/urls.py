"""
The django.conf.urls.static now becomes django django.urls in 2.0.2
The path replaces the url function in django 2.0.2
"""
from django.urls import path  # , re_path
from . import views

urlpatterns = [
    path('', views.index, name='welcome'),
]
