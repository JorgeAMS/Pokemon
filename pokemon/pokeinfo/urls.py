from django.urls import path
from django.shortcuts import render
from . import views

app_name='pokeinfo'
urlpatterns = [
    path('', views.MainView.as_view(), name='mainview'),
    path('poke_service/', views.ServiceView.as_view(), name='webservice')
]