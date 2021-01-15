from django.db import models
from apps.autor.models import Autor
from django.db.models.signals import post_delete

# Create your models here.
from apps.libro.models import Libro
from .managers import PrestamoManager

class Lector(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombres

class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector, 
        on_delete=models.CASCADE
        )
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE, 
        related_name='libro_prestamo')
    fecha_prestamos = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    stock = models.PositiveIntegerField(default=0)

    objects = PrestamoManager()

    def __str__(self):
        return self.libro.titulo


# Podemos mandar los signals a un nuevo archivo, y por claridad importartlos aquí
from .signals import update_libro_stock

# def update_libro_stock(sender, instance, **kwargs):
#     instance.libro.stock +=1
#     instance.libro.save()

# Y hacemos aquí la conexión, y ordenamos mejor el código.
post_delete.connect(update_libro_stock, sender=Prestamo)