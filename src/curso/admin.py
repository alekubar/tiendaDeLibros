
from django.contrib import admin
from .models import Comision, Curso, Alumno

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
    list_display = ("curso__nombre","numero", "fecha_inicio")

@admin.register(Alumno)
class Alumno(admin.ModelAdmin):
    list_display = ("comision", "dni") 