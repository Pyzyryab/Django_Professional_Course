from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListaLibros.as_view(), name='libros'),
]