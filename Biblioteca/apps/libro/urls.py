from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListaLibros.as_view(), name='libros'),
    path('libros-categoria/', views.ListaLibrosCategoria.as_view(), name='libros_categoria'),
    path('libros-detalle/<pk>', views.LibroDetailView.as_view(), name='libro_detalle'),
    path('libros-triagram', views.ListaLibrosTriagram.as_view(), name='lista_libros_triagram'),
]
