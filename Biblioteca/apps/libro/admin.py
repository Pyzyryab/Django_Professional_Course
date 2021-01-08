from django.contrib import admin

# Register your models here.
from .models import Libro, Categoria
admin.site.register(Libro)
admin.site.register(Categoria)