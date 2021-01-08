from django.contrib import admin

# Register your models here.
from .models import Lector, Prestamo
admin.site.register(Lector)
admin.site.register(Prestamo)