from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):
    contraseña_usuario = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ('nombre_usuario',
                  'apellido_usuario',
                  'contraseña_usuario',
                  'estado_usuario',
                  'ci_usuario',
                  'telefono_usuario',
                  'direccion_usuario',
                  'descripcion_usuario')



