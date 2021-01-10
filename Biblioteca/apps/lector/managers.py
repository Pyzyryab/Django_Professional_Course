from django.db import models
from django.db.models import Avg, Sum, Count
from django.db.models.functions import Lower

class PrestamoManager(models.Manager):

    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id='1' #Así filtraríamos todos los préstamos que se han hecho de un libro con id=x

        ).aggregate( #podemos aplicar tantas funciones aritméticas como queramos con aggregate
            promedio_edad = Avg('lector__edad'),
            suma_edad = Sum('lector__edad'),
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            'libro'
        ).annotate( #Annotate necesita de un identificador por el cual agrupar y realizar la operación aritmética que se le pide
            num_prestados=Count('libro'),
            titulo=Lower('libro__titulo'),
        )

        for r in resultado:
            print(r, r['num_prestados'])

        return resultado #!Ojo, tenemos otro manager en la aplicación libro, que lo consulta también desde el related name.

        ''' Cuando usamos annotate, este nos requiere un parámetro para agrupar chismes.
        En este caso, annotate usa values
        '''