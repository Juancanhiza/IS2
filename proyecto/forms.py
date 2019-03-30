from django import forms

from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    fecha_inicio_proyecto = forms.DateTimeField()
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'descripcion')

