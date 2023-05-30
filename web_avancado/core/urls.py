from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/w3c', views.w3c, name="w3c"),
    path('/html', views.html, name="html"),
]