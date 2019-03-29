from django import forms

from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    fecha_inicio_proyecto = forms.DateTimeField()
    class Meta:
        model = Proyecto
        fields = ('nombre_proyecto', 'fecha_inicio_proyecto', 'fecha_fin_proyecto', 'estado_proyecto', 'descripcion_proyecto')

