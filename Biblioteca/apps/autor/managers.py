from django.db import models


# A manager it's a funtion that belongs to a unique db model.

class AutorMagager(models.Manager):
    '''Managers from Autor model'''

    def list_authors(self):
        return self.all() 

    def buscar_autor(self, kword):
        
        # resultado = self.filter(nombre=kword) #Filtrar por un atributo específico y que sea exactamente igual al requerido en kword
        resultado = self.filter(
            nombre__icontains=kword,
            ) # Filtra por atributo que contenga kword. Específico de la ORM de Django

        return resultado
    '''Los managers no necesitan importar los modelos si quiera. Son funciones
    en las cuales declaramos la consulta que nosotros deseamos realizar a base de datos'''