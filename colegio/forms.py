from django import forms
from colegio.models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['dni', 'nombre', 'apellidos']