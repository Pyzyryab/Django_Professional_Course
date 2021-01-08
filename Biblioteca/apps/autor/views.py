from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Autor

class ListaAutores(ListView):
    # model = Autor
    context_object_name = 'lista_autores'
    template_name = "autor/lista.html"

    def get_queryset(self):
        
        input = self.request.GET.get("kword", '')

        if input == '':
            return Autor.objects.list_authors()
        else:
            return Autor.objects.buscar_autor(input.capitalize())
        