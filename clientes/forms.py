from django import forms
from .models import Cliente

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','ruc','direccion','telefono','descripcion')

class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'ruc', 'direccion', 'telefono', 'descripcion')

