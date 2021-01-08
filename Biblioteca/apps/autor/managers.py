from django.db import models
from django.db.models import Q # Esto es para importar el operador OR
# Para el operador & se pasa con una simple coma entre parámtros


# A manager it's a funtion that belongs to a unique db model.

class AutorMagager(models.Manager):
    '''Managers from Autor model'''

    def list_authors(self):
        return self.all() 

    def buscar_autor(self, kword):
        # resultado = self.filter(nombre=kword) #Filtrar por un atributo específico y que sea exactamente igual al requerido en kword
        # Esta parte es la encargada de transformar la consulta a BBDD
        resultado = self.filter(
            nombre__icontains=kword,
            ) # Filtra por atributo que contenga kword. Específico de la ORM de Django

        return resultado
    '''Los managers no necesitan importar los modelos si quiera. Son funciones
    en las cuales declaramos la consulta que nosotros deseamos realizar a base de datos'''

    def buscar_autor_nombreyapellidos(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword) # Consulta OR
        )
        return resultado

    def buscar_autor_filtro_exclude(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword) # Consulta OR
        ).exclude(edad=70)

        #! OJO, my importante. Dentro del exclude podríamos pasar el parámetro Q y dentro de filter poner
        #! otro tipo de consulta
        '''#!resultado = self.filter(
            nombre__icontains=kword,
            ).exclude(
                (edad__icontains=70) | Q(edad__icontains=50)
            ) #! Tambien podemos hacer un filtro dentro de otro filtro :)
        '''
        return resultado

    def buscar_autor_mayor_menor_que(self, kword):
        resultado = self.filter(
            edad__gt=40,
            edad__lt=80,
            ).order_by('apellidos', 'nombre') #! OJO, se le puede pasar un método directo a filter para ordenar
        return resultado