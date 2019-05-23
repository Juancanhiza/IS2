from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


@method_decorator(login_required, name='dispatch')
class UserListView(LoginRequiredMixin, ListView):
    """
    Vista de la lista de Usuarios
    """
    template_name = 'usuarios/list.html'
    model = Usuario
    queryset = Usuario.objects.all()

    def get(self, request, *args, **kwargs):
        self.object_list = Usuario.objects.all()
        permisos = request.user.get_nombres_permisos()
        return self.render_to_response(self.get_context_data(permisos=permisos))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Usuarios"
        return context


@method_decorator(login_required, name='dispatch')
class CreateUserView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Vista para la creacion de un Usuario
    """
    template_name = 'usuarios/user.html'
    model = Usuario
    success_url = '/usuarios/'
    form_class = CreateUserForm
    success_message = 'Se ha creado el usuario'

    def get(self, request, *args, **kwargs):
        self.object = None
        permisos = request.user.get_nombres_permisos()
        return self.render_to_response(self.get_context_data(permisos=permisos))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Usuario"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Vista para la modificacion de un Usuario
    """
    template_name = 'usuarios/user.html'
    model = Usuario
    form_class = UpdateUserForm
    success_url = '/usuarios/'
    success_message = 'Los cambios se guardaron correctamente'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permisos = request.user.get_nombres_permisos()
        return self.render_to_response(self.get_context_data(permisos=permisos))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Usuario " + str(self.object.pk)
        return context

    def get_object(self, queryset=None):
        return Usuario.objects.get(pk=self.kwargs['pk'])


@method_decorator(login_required, name='dispatch')
class VerUserDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    """
    Vista de los detalles de un Usuario
    """
    model = Usuario
    template_name = 'usuarios/ver_user.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permisos = request.user.get_nombres_permisos()
        return self.render_to_response(self.get_context_data(permisos=permisos))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ver Usuario " + str(self.object.pk)
        return context

    def get_object(self, queryset=None):
        return Usuario.objects.get(pk=self.kwargs['pk'])