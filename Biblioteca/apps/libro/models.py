from django.db import models
from apps.autor.models import Autor

from .managers import LibroManager, CategoriaManager

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{str(self.id)} - {self.nombre}' 

    objects = CategoriaManager()

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, 
        on_delete=models.CASCADE, 
        related_name='categoria_libro', # Atributo para darle acceder al foreign key al revés, haciendo que "internamente" categoría tenga un atributo que relacione ese modelo con libro.
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

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo', 'fecha']

        # Para conseguir acceder y modificar el nombre que la ORM de Django guarda en BBDD
        db_table = 'Libro'

        # Para que la combinación de X campos sea única
        unique_together = ['titulo', 'fecha']

    def __str__(self):
        return f'{str(self.id)} - {self.titulo}'