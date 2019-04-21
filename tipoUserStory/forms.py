from django import forms

from .models import TipoUserStory

class CreateUserStoryTypeForm(forms.ModelForm):
    class Meta:
        model = TipoUserStory
        fields = ('nombre', 'descripcion')

class UpdateUserStoryTypeForm(forms.ModelForm):
    class Meta:
        model = TipoUserStory
        fields = ('nombre', 'descripcion')

