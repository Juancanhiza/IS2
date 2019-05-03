from django import forms
from .models import *

class CreateUserStoryForm(forms.ModelForm):
    fecha_inicio= forms.DateTimeField()
    class Meta:
        model = UserStory
        fields = ('proyecto',
                  'nombre',
                  'descripcion',
                  'fecha_inicio',
                  'duracion_estimada',
                  'valor_negocio',
                  'prioridad',
                  'valor_tecnico',
                  'team_member',
                  'sprint',
                  'tipo_us',
                  'flujo',
                  'fase',
                  'estado_fase'
                  )

class UpdateUserStoryForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField()
    class Meta:
        model = UserStory
        fields = ('proyecto',
                  'nombre',
                  'descripcion',
                  'fecha_inicio',
                  'duracion_estimada',
                  'valor_negocio',
                  'prioridad',
                  'valor_tecnico',
                  'team_member',
                  'sprint',
                  'tipo_us',
                  'flujo',
                  'fase',
                  'estado_fase',
                  )


class ActividadForm(forms.ModelForm):
    """
    Formulario para subir archivos al User story
    """
    class Meta:
        model = Actividad
        fields = ('nombre',
                  'descripcion',
                  'duracion',
                  )


class ArchivoForm(forms.ModelForm):
    """
    Formulario para subir archivos al User Story
    """
    class Meta:
        model = Archivo
        """Campos a ingresar"""
        fields = ('titulo', 'archivo', )


class NotaForm(forms.ModelForm):
    """
    Formulario para subir notas al User Story
    """
    class Meta:
        model = Nota
        """Campos a ingresar"""
        fields = ('nota',)


class GuardarNotaForm(forms.ModelForm):
    """
    Formulario para subir notas al User Story
    """
    class Meta:
        model = Nota
        """Campos a ingresar"""
        fields = ('us','usuario','nota',)