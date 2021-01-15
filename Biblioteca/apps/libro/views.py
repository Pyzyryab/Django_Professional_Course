from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Libro

class ListaLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        
        input = self.request.GET.get("kword", '') #! OJO, es una tupla que recibe cómo segundo parámetro string vacío
        #!Recogemos los campos datetime pasados en el HTML
        fecha_inicio = self.request.GET.get("fecha_inicio", '')
        fecha_fin = self.request.GET.get("fecha_fin", '')
        
        if fecha_inicio and fecha_fin:
            return Libro.objects.lista_libros_nombre_fechas(input, fecha_inicio, fecha_fin)
        else:
            return Libro.objects.lista_libros_completa

class ListaLibrosCategoria(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista_categoria.html'

    def get_queryset(self):
        
        return Libro.objects.listar_libros_categoria('1')

        # return Libro.objects.lista_libros_completa

class LibroDetailView(DetailView): # Las detail view pasan internamente el context automáticamente
    model = Libro
    template_name = 'libro/libro_detail.html'

class ListaLibrosTriagram(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        
        input = self.request.GET.get("kword", '') 
        return Libro.objects.lista_libros_triagram(input)

# El siguiente código se escribe de manera educativa, y con el mero hecho de guardarlo como una referencia.
# El siguiente ejemplo es de como realizar validaciones sobre un libro que hayamos prestado a un lector
# Usaremos la función de la ORM de Django get_or_create, la cual busca un registro en BBDD si existe.
# Si existe, nos devuelve el objeto, y si no lo crea. Esto es un shotcut para validaciones, por ejemplo, 
# para validad si UN lector en concreto ya tiene en préstamo un libro que intenta que se le vuelva a prestar.
'''
class Prestamo(FormView):
    
    template_name = 'lector/lista.html' # Por comodidad, usamos la APP libro como base de anotaciones, aunque sea algo de otra APP 
    form_class = 'NuestroFormularioPréstamo'
    success_url = '.' # Indica recargar la misma URL

    def form_valid(self, form):

        obj, created = Prestamo.objects.get_or_create  (
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto=False,
            defaults={
                'fecha_prestamo': date.today()
            }
        )      

    # get_or_create devuelve una tupla, el objeto y un boolean
    # procedemos a validar si el lector ya tiene el libro que solita en préstamo

    if created:
        return super(Prestamo, self).form_valid(form)
    else:
        return HttpResponseRedirect('/')
'''

#! Aquí ahora, haremos un registro de múltiples préstamos a un usuario.
# Por ser más conciso, y resumir el código en un lugar, escribiremos aquí el formulario, 
# aunque lo recomendado sería que lo escribieran en su correspondiente forms.py, dentor de su APP

'''
//Primero el formulario
class MultiplePrestamoForm(forms.ModelForm):

    libros = forms.ModelMultipleChoiceField(
        queryset = None,
        required = True,
        widget=forms.CheckboxSelectMultiple,

    )

    class Meta:
        model = Prestamo
        field = (
            lector, # Sólo necesitamos un campo, en este caso el lector que solicita los préstamos
        )

    //
    # Llamamos al constructor para que se muestre con un valor determidao HTML, 
    sobreescribiéndolo

    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = Libro.objects.all()
    
//TODO ojo, ahora es cuando volcaremos lo que nos devuelve el formulario en nuestra vista.
//! Importante, el campo LIBRO de nuestro formulario nos devuelve una lista!! (queryset)

class AddMultiplePrestamo(formView):
    template_name = 'lector/multiple.html' # Por comodidad, usamos la APP libro como base de anotaciones, aunque sea algo de otra APP 
    form_class = 'MultiplePrestamoForm'
    success_url = '.' # Indica recargar la misma URL

    def form_valid(self, form):

        # Iteramos el queryset para recuperar los datos acorde a como debemos de guardarlos en BBDD
        for libro in form.cleaned_data['libro']:
            prestamo = Prestamo(
                lector=form.cleaned_data['lector'],
                libro=libro=
                fecha_prestamo=date.today(),
                devuelto=False, #Iteramos los campos OBLIGATORIOS DE NUESTRO MODELO
            )

        return super(AddMultiplePrestamo, self).super()

'''