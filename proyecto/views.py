from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Proyecto
from proyecto.forms import CreateProjectForm, UpdateProjectForm
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
class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'proyecto/list.html'
    model = Proyecto
    queryset = Proyecto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Proyectos"
        return context


@method_decorator(login_required, name='dispatch')
class CreateProjectView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'proyecto/proyecto.html'
    model = Proyecto
    success_url = './'
    form_class = CreateProjectForm
    success_message = 'Se ha creado el proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Proyecto"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateProjectView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'proyecto/proyecto.html'
    model = Proyecto
    form_class = UpdateProjectForm
    success_url = './'
    success_message = 'Los cambios se guardaron correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Proyecto"
        return context

    def get_object(self, queryset=None):
        return Proyecto.objects.get(pk=self.kwargs['pk'])

    def get_absolute_url(self):
        return reverse('update_rol', kwargs={'pk': self.kwargs['pk']})

