from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Sprint
from proyecto.models import Proyecto
from sprint.forms import CreateSprintForm, UpdateSprintForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
"""
Vista del Login
"""

@method_decorator(login_required, name='dispatch')
class SprintListView(LoginRequiredMixin, ListView):
    template_name = 'sprint/list.html'
    model = Sprint
    queryset = Sprint.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Sprints de Proyecto"
        return context

    def get(self,request,*args,**kwargs):
        self.object = None
        self.object_list = Sprint.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(project=proyecto, object_list=self.object_list))


@method_decorator(login_required, name='dispatch')
class CreateSprintView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'sprint/sprint.html'
    model = Sprint
    success_url = './'
    form_class = CreateSprintForm
    success_message = 'Se ha creado el sprint'

    def get_object(self, queryset=None):
        obj = Sprint()
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
        context['title'] = "Crear Sprint"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateSprintView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'sprint/sprint.html'
    model = Sprint
    form_class = UpdateSprintForm
    success_url = './'
    success_message = 'Los cambios se guardaron correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Sprint"
        return context

    def get_object(self, queryset=None):
        return Sprint.objects.get(pk=self.kwargs['pk'])

    def get_absolute_url(self):
        return reverse('update_rol', kwargs={'pk': self.kwargs['pk']})

