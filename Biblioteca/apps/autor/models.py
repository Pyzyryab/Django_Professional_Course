from django.db import models
from django.db.models.fields import CharField

from .managers import AutorMagager

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()

    #Conexión del manager con el autor
    objects = AutorMagager()

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'