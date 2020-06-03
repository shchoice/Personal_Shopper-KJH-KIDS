from django.contrib import admin
from django.urls import path
from . import views

app_name = 'styles'

urlpatterns = [
    path('', views.StylesList, name='styles'),
    path('main2', views.main2),
]
