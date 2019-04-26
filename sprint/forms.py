from django import forms

from .models import Sprint

class CreateSprintForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    duracion = forms.DurationField()
    class Meta:
        model = Sprint
        fields = ('proyecto','nombre', 'fecha_inicio', 'fecha_fin', 'duracion')

class UpdateSprintForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    duracion = forms.DurationField()
    class Meta:
        model = Sprint
        fields = ('proyecto','nombre', 'fecha_inicio', 'fecha_fin', 'duracion')