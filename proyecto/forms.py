from django import forms
from django.forms import inlineformset_factory
from .models import *


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_ini_estimada', 'fecha_fin_estimada', 'estado', 'descripcion')

    widgets = {
        'fecha_ini_estimada': forms.DateField(),
        'fecha_fin_estimada': forms.DateField()
    }


class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_ini_estimada', 'fecha_fin_estimada', 'estado', 'descripcion')

    widgets = {
        'fecha_ini_estimada': forms.DateField(),
        'fecha_fin_estimada': forms.DateField()
    }

    labels = {
        'nombre': 'Nombre del Proyecto',
        'fecha_inicio': 'Fecha de Inicio',
        'fecha_fin': 'Fecha de Fin',
        'estado': 'Estado',
        'descripcion': 'Descripcion ',

    }


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        exclude = ()
        fields = ('usuario', 'rol')


TeamMemberFormSet = inlineformset_factory(Proyecto, TeamMember, form=TeamMemberForm, extra=1)