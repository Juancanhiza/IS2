from django import forms
from django.forms import inlineformset_factory
from .models import *

class CreateProjectForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'descripcion')

class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'descripcion')

class ProyectoDetalleForm(forms.ModelForm):
    class Meta:
        model = ProyectoDetalle
        exclude = ()
        fields = ('usuario','rol')

ProyectoDetalleFormSet = inlineformset_factory(Proyecto,ProyectoDetalle,form=ProyectoDetalleForm,extra=1)



