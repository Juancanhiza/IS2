from django import forms
from .models import UserStory
from django.core.validators import MaxValueValidator

class CreateUserStoryForm(forms.ModelForm):
    fecha_inicio= forms.DateTimeField()
    class Meta:
        model = UserStory
        fields = ('nombre',
                  'descripcion',
                  'fecha_inicio',
                  'duracion_estimada',
                  'valor_negocio',
                  'prioridad',
                  'valor_tecnico')

class UpdateUserStoryForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField()
    class Meta:
        model = UserStory
        fields = ('nombre',
                  'descripcion',
                  'fecha_inicio',
                  'duracion_estimada',
                  'valor_negocio',
                  'prioridad',
                  'valor_tecnico'
                  )
