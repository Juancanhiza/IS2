from django import forms

from .models import Proyecto

class CreateProjectForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'descripcion')

class UpdateProjectForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'descripcion')

