from django import forms
from django.forms import inlineformset_factory
from .models import *


class CreateFlujoForm(forms.ModelForm):
    class Meta:
        model = Flujo
        fields = ('nombre','proyecto','descripcion')
    widgets = {
        'proyecto': forms.HiddenInput()
    }


class UpdateFlujoForm(forms.ModelForm):
    class Meta:
        model = Flujo
        fields = ('nombre','proyecto','descripcion')
    widgets = {
        'proyecto': forms.HiddenInput()
    }


class FaseForm(forms.ModelForm):
    class Meta:
        model = Fase
        exclude = ()
        fields = ('nombre',)


FaseFormSet = inlineformset_factory(Flujo, Fase, form=FaseForm, extra=1)
