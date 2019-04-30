from django import forms
from .models import Sprint


class CreateSprintForm(forms.ModelForm):

    class Meta:
        model = Sprint
        fields = ('proyecto', 'nombre', 'fecha_ini_estimada', 'fecha_fin_estimada','estado')

    widgets = {
        'fecha_ini_estimada': forms.DateField(),
        'fecha_fin_estimada': forms.DateField()
    }


class UpdateSprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ('proyecto','nombre', 'fecha_ini_estimada', 'fecha_fin_estimada','estado')

    widgets = {
        'fecha_ini_estimada': forms.DateField(),
        'fecha_fin_estimada': forms.DateField()
    }