from django import forms
from .models import UserStory
from django.core.validators import MaxValueValidator

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
                  'sprint'
                  )