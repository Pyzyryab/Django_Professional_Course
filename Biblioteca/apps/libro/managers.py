from django.db import models
from django.db.models import Q # Esto es para importar el operador OR
from django.db.models import Count # Esto es para importar el operador OR

from django.contrib.postgres.search import TrigramSimilarity

# Para el operador & se pasa con una simple coma entre parámtros

class LibroManager(models.Manager):
    '''Managers from Autor model'''

    def lista_libros_triagram(self, kword):
        if kword:
            resultado = self.filter(
                titulo__triagram_similar=kword,
                )
            return resultado
        else:
            return self.all()[:10]


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
        fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d').date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(fecha_inicio, fecha_fin)
            ) 
        return resultado

    def listar_libros_categoria(self, categoria):

        return self.filter(
            categoria__id = categoria
        ).order_by('titulo')

    def add_autor_libro(self, libro_id, autor): #manager para encargárse de añadir autores para un libro en código
        libro = self.get(id=libro_id) # get recupera una única consulta. Libro.objects == self.
        libro.autores.add(autor) #añade algo en un many to many a través de un manager
        # libro.autores.remove(autor) #borra un registro a través del manager
        #Obviamente, desde el html podríamos poner un FORM con un Entry Text para que guarde/elimine (o sea el caso que sea) el registro que sea
        # pero no con Detail View. Podríamos con Mixin o FormView
        return libro

    def libros_num_prestamos(self): #!número de veces prestado un libro. Ncesitamos agregar related name en el modelo préstamo para poder acceder desde libro
        #! ESTO NOS DEVUELVE LOS DATOS EN FORMA DE DICT de Python, el aggregate
        # libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo') [en el modelo de Préstamo, app: Lector]
        resultado = self.aggregate(
            num_prestamos = Count('libro_prestamo') # queremos contar el númeor de libros que tiene X categoría, y accediendo por Foreign Key inversa == related_name
        )
        return resultado

    ''' #! Usaríamos aggregate cuando nos interese devolver una estructura de datos concreta, como DICT. 
    En caso de querer un Queryset, usaríamos Annotate.'''

    def num_libros_prestados(self):
        resultado = self.annotate( #Annotate necesita de un identificador por el cual agrupar y realizar la operación aritmética que se le pide
            num_prestados=Count('libro_prestamo')
        )
        return resultado

class CategoriaManager(models.Manager):
    '''Managers for Categoría model'''

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct() #hace que no nos repita valores de las consultas innecesariamente

    def listar_categoria_libros(self): #!Este manager introduce la función annotate() de la ORM de Django, válida para facilitar operaciones aritméticas
        resultado = self.annotate(
            num_libros = Count('categoria_libro') # queremos contar el númeor de libros que tiene X categoría, y accediendo por Foreign Key inversa == related_name
        )
        for categoria in resultado: #! Sólo para comprobar los resultados yendo a 'python manage.py shell' 
            print('********')
            print(categoria, categoria.num_libros)
        return resultado

