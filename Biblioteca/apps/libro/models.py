from django.db import models
from apps.autor.models import Autor

from .managers import LibroManager, CategoriaManager

from django.db.models.signals import post_save

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

        # Para hacer validaciones SIMPLES (las validaciones mejor en los managers, pero si se trata de algo)
        # simple podemos usar el atributo #!'constraints'). 
        # Pongamos un ejemplo básico, de un modelo que representa a una persona,
        # con un campo EDAD y que esa persona para registrarla en nuestra BBDD tiene que ser mayor a 18.
        '''
        class Persona(models.Model):
            edad = models.IntegerField()
            class Meta:
                constraints = [
                    models.CheckConstraint(check=models.Q(edad__gte=18), name='Edad Mayor a 18')
                ] # gte representa >
                abstract = True 

        Dado que no tenemos ningún atributo decente al que asignarle esta restricción, la dejamos como un comentario
        a modo recordatorio con fines educativos.

        Incluso siguiendo con la lógica de persona, podríamos definir un nuevo modelo
        
        class Empleado(Persona):
            empleo = models.CharField('Empleo', max_length=30)

        Entonces a través de la herencia simple, haríamos que EMPLEADO TENGA TODOS LOS CAMPOS
        que se hayan creado en PERSONA. Como es lógico, y no tendría sentido tener en nuestra BBDD repetidos
        los campos que ha heredado, podemos indicarle a persona a través del atributo 'abstract' que NO
        queremos que se cree la tabla Persona en base de datos
        
        '''
        
    def __str__(self):
        return f'{str(self.id)} - {self.titulo}'