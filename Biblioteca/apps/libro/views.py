from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Libro

class ListaLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        
        input = self.request.GET.get("kword", '') #! OJO, es una tupla que recibe cómo segundo parámetro string vacío
        #!Recogemos los campos datetime pasados en el HTML
        fecha_inicio = self.request.GET.get("fecha_inicio", '')
        fecha_fin = self.request.GET.get("fecha_fin", '')
        
        if fecha_inicio and fecha_fin:
            return Libro.objects.lista_libros_nombre_fechas(input, fecha_inicio, fecha_fin)
        else:
            return Libro.objects.lista_libros_completa

class ListaLibrosCategoria(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista_categoria.html'

    def get_queryset(self):
        
        return Libro.objects.listar_libros_categoria('1')

        # return Libro.objects.lista_libros_completa

class LibroDetailView(DetailView): # Las detail view pasan internamente el context automáticamente
    model = Libro
    template_name = 'libro/libro_detail.html'

class ListaLibrosTriagram(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        
        input = self.request.GET.get("kword", '') 
        return Libro.objects.lista_libros_triagram(input)