from django import forms
from .models import Cliente

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','descripcion','direccion','ruc','telefono')

class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','descripcion','direccion','ruc','telefono')

