from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre_cliente','descripcion_cliente','direccion_cliente','ruc_cliente','telefono_cliente')

