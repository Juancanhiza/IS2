from django import forms
from rol.models import *
from django import forms
from django.forms import CharField, Form

#class BuscarRol(Form):
#    """
#    Formulario para buscar un Rol por nombre
#    """
#    Nombre = CharField()

class CreateRolForm(forms.ModelForm):
    """
    Formulario para crear un Rol
    """
    class Meta:
        model = Rol
        fields = [
            'nombre',
            'descripcion',
            'permisos'
        ]
        labels = {
            'nombre': 'Nombre del rol',
            'descripcion': 'Descripcion ',
            'permisos': 'Permisos',

        }
        widgets = {
        'permisos': forms.CheckboxSelectMultiple(),
        }
    def clean_permiso(self):
        permisos = self.cleaned_data['permisos']
        try:
            pr = Permiso.objects.get(permisos = permisos)
        except:
            return self.cleaned_data['permisos']
        raise forms.ValidationError('Debe seleccionar al menos uno')


class UpdateRolForm(forms.ModelForm):
    """
    Formulario para modificar un Rol
    """
    class Meta:
        model = Rol
        fields = [
            'nombre',
            'descripcion',
            'permisos'
        ]
        labels = {
            'nombre': 'Nombre del rol',
            'descripcion': 'Descripcion ',
            'permisos': 'Permisos',

        }
        widgets = {
        'permisos': forms.CheckboxSelectMultiple(),
        }
    def clean_permiso(self):
        permisos = self.cleaned_data['permisos']
        try:
            pr = Permiso.objects.get(permisos = permisos)
        except:
            return self.cleaned_data['permisos']
        raise forms.ValidationError('Debe seleccionar al menos uno')