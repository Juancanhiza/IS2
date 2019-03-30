from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Rol
from django.contrib.auth.models import User
from rol.forms import RolForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@method_decorator(login_required, name='dispatch')
class RolListView(LoginRequiredMixin, ListView):
    template_name = 'rol/rollist.html'
    model = Rol
    queryset = Rol.objects.all()


@method_decorator(login_required, name='dispatch')
class CreateRolView(LoginRequiredMixin, CreateView):
    template_name = 'rol/rol.html'
    model = Rol
    form_class = RolForm


@method_decorator(login_required, name='dispatch')
class UpdateRolView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'rol/rol.html'
    model = Rol
    fields = ['nombre','descripcion','permisos']
    success_message = 'Los cambios se guardaron correctamente'

    def get_object(self, queryset=None):
        return Rol.objects.get(pk=self.kwargs['pk'])

    def get_absolute_url(self):
        return reverse('update_rol', kwargs={'pk': self.kwargs['pk']})
