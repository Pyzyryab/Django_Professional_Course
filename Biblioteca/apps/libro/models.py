from django.db import models
from apps.autor.models import Autor

from .managers import LibroManager

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{str(self.id)} - {self.nombre}' 

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, 
        on_delete=models.CASCADE, 
        related_name='categoria_libro',
        # default=5,
        blank=True, 
        null=True
        )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento', )
    portada = models.ImageField(upload_to='portada', blank=True, null=True)
    visitas = models.PositiveIntegerField()

    objects = LibroManager()

    def __str__(self):
        return self.titulo