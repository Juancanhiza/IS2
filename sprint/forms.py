from django import forms
from .models import Sprint


class CreateSprintForm(forms.ModelForm):
    """
    Formulario para la creacion de un nuevo Sprint
    """
    class Meta:
        model = Sprint
        fields = ('proyecto', 'nombre', 'fecha_ini_estimada', 'fecha_fin_estimada','estado')

        widgets = {
            'proyecto': forms.HiddenInput(),
        }


class UpdateSprintForm(forms.ModelForm):
    """
    Formulario para la modificacion de un Sprint
    """
    class Meta:
        model = Sprint
        fields = ('proyecto','nombre', 'fecha_ini_estimada', 'fecha_fin_estimada','estado')

        widgets = {
            'proyecto': forms.HiddenInput(),
        }
