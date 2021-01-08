from django.db import models
from django.db.models import Q # Esto es para importar el operador OR
# Para el operador & se pasa con una simple coma entre parámtros

class LibroManager(models.Manager):
    '''Managers from Autor model'''

    def lista_libros_completa(self):
        return self.all() 

    def lista_libros(self, kword):

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('1960-01-01','2007-01-01')
            ) 
        return resultado

    def lista_libros_nombre_fechas(self, kword, fecha_inicio, fecha_fin):
        
        #Por si acaso el rango de fechas es inválido
        import datetime

        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()        
        fecha_FIN = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d').date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(fecha_inicio, fecha_fin)
            ) 
        return resultado

