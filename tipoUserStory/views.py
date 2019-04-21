from django.views.generic import ListView, CreateView, UpdateView
from .models import TipoUserStory
from tipoUserStory.forms import CreateUserStoryTypeForm, UpdateUserStoryTypeForm
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@method_decorator(login_required, name='dispatch')
class tipoUserStoryListView(LoginRequiredMixin, ListView):
    template_name = 'tipoUserStory/list.html'
    model = TipoUserStory
    queryset = TipoUserStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Tipos de User Stories"
        return context

@method_decorator(login_required, name='dispatch')
class CreateUserStoryTypeView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'tipoUserStory/tipoUserStory.html'
    model = TipoUserStory
    success_url = './'
    form_class = CreateUserStoryTypeForm
    success_message = 'Se ha creado el tipo de User Story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Tipo de User Story"
        return context

@method_decorator(login_required, name='dispatch')
class UpdateUserStoryTypeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'tipoUserStory/tipoUserStory.html'
    model = TipoUserStory
    success_url = './'
    form_class = UpdateUserStoryTypeForm
    success_message = 'Los cambios se guardaron correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Tipo de User Story"
        return context

    def get_object(self, queryset=None):
        return TipoUserStory.objects.get(pk=self.kwargs['pk'])

    def get_absolute_url(self):
        return reverse('update_rol', kwargs={'pk': self.kwargs['pk']})