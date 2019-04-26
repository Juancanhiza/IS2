from django.views.generic import ListView, CreateView, UpdateView
from .models import TipoUserStory
from tipoUserStory.forms import CreateUserStoryTypeForm, UpdateUserStoryTypeForm
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from proyecto.models import *
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

    def get(self,request,*args,**kwargs):
        self.object = None
        self.object_list = TipoUserStory.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(project=proyecto, object_list=self.object_list))

@method_decorator(login_required, name='dispatch')
class CreateUserStoryTypeView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'tipoUserStory/tipoUserStory.html'
    model = TipoUserStory
    success_url = '../'
    form_class = CreateUserStoryTypeForm
    success_message = 'Se ha creado el tipo de User Story'

    def get_object(self, queryset=None):
        obj = TipoUserStory()
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        obj.proyecto = proyecto
        return obj

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Tipo de User Story"
        return context

@method_decorator(login_required, name='dispatch')
class UpdateUserStoryTypeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'tipoUserStory/tipoUserStory.html'
    model = TipoUserStory
    success_url = '../'
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