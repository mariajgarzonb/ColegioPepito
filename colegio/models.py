from django.db import models
from django.utils.html import format_html



# Create your models here.



class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    horas = models.PositiveSmallIntegerField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.horas)

    def coloreado(self):
        if self.horas >= 4:
            return format_html('<span style="color: blue;">{0}</span>'.format(self.nombre))
        else:
            return format_html('<span style="color: red;">{0}</span>'.format(self.nombre))


class Alumno(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellidos)

    def coloreado(self):
        return format_html('<span style="color: blue;">{0} {1}</span>'.format(self.nombre, self.apellidos))