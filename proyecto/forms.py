from django import forms

from .models import Proyecto

class CreateProjectForm(forms.ModelForm):
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'descripcion')

class UpdateProjectForm(forms.ModelForm):
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'descripcion')

