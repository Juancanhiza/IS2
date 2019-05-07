from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Cliente
from clientes.forms import CreateClientForm, UpdateClientForm
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


@method_decorator(login_required, name='dispatch')
class ClientListView(LoginRequiredMixin, ListView):
    template_name = 'clientes/list.html'
    model = Cliente
    queryset = Cliente.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Clientes"
        return context


@method_decorator(login_required, name='dispatch')
class CreateClientView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'clientes/cliente.html'
    model = Cliente
    success_url = './'
    form_class = CreateClientForm
    success_message = 'Se ha creado el cliente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Cliente"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateClientView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'clientes/cliente.html'
    model = Cliente
    form_class = UpdateClientForm
    success_url = './'
    success_message = 'Los cambios se guardaron correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Cliente"
        return context

    def get_object(self, queryset=None):
        return Cliente.objects.get(pk=self.kwargs['pk'])

    def get_absolute_url(self):
        return reverse('update_client', kwargs={'pk': self.kwargs['pk']})

@method_decorator(login_required, name='dispatch')
class VerClientDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Cliente
    template_name = 'clientes/ver_cliente.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ver Cliente"
        return context

    def get_object(self, queryset=None):
        return Cliente.objects.get(pk=self.kwargs['pk'])