from django import forms
from .models import TipoUserStory

class CreateUserStoryTypeForm(forms.ModelForm):
    class Meta:
        model = TipoUserStory
        fields = ('proyecto','nombre', 'descripcion','flujos')

        widgets = {
            'flujos': forms.CheckboxSelectMultiple(),
            'proyecto': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserStoryTypeForm, self).__init__(*args, **kwargs)
        self.fields['proyecto'].widget = forms.HiddenInput()

class UpdateUserStoryTypeForm(forms.ModelForm):
    class Meta:
        model = TipoUserStory
        fields = ('proyecto','nombre', 'descripcion','flujos')

        widgets = {
            'flujos': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateUserStoryTypeForm, self).__init__(*args, **kwargs)
        self.fields['proyecto'].widget = forms.HiddenInput()