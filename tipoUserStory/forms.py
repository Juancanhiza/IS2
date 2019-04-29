from django import forms
from .models import TipoUserStory

class CreateUserStoryTypeForm(forms.ModelForm):
    class Meta:
        model = TipoUserStory
        fields = ('proyecto','nombre', 'descripcion','flujos')

class UpdateUserStoryTypeForm(forms.ModelForm):
    class Meta:
        model = TipoUserStory
        fields = ('proyecto','nombre', 'descripcion','flujos')


