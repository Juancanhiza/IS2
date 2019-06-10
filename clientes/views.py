from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Cliente
from clientes.forms import CreateClientForm, UpdateClientForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
"""
Vistas necesarias para la administracion de Cliente
"""

@method_decorator(login_required, name='dispatch')
class ClientListView(LoginRequiredMixin, ListView):
    """
    Clase de la vista de lista de Clientes
    """
    template_name = 'clientes/list.html'
    model = Cliente
    queryset = Cliente.objects.all()

    def get(self,request,*args,**kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object_list = Cliente.objects.all()
        permisos = request.user.get_nombres_permisos()
        return self.render_to_response(self.get_context_data(object_list=self.object_list, permisos=permisos))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super().get_context_data(**kwargs)
        context['title'] = "Clientes"
        context['direccion'] = {}
        context['direccion']['Clientes'] = (1, '/clientes/')
        return context


@method_decorator(login_required, name='dispatch')
class CreateClientView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Clase de la vista de Creacion de Cliente
    """
    template_name = 'clientes/cliente.html'
    model = Cliente
    success_url = '../'
    form_class = CreateClientForm
    success_message = 'Se ha creado el cliente'

    def get(self,request,*args,**kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        permisos = request.user.get_nombres_permisos()
        return self.render_to_response(self.get_context_data(permisos=permisos, form=form))


    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Cliente"
        context['direccion'] = {}
        context['direccion']['Clientes'] = (1, '/clientes/')
        context['direccion']['Crear Cliente'] = (2,'/clientes/create/')
        return context

    def post(self, request, *args, **kwargs):
        """
        Metodo que es ejecutado al darse una consulta POST
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta POST
        """
        self.object = None
        formclass = self.get_form_class()
        form = self.get_form(formclass)
        permisos = request.user.get_nombres_permisos()
        if form.is_valid():
            self.object = form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(permisos=permisos,form=form))



@method_decorator(login_required, name='dispatch')
class UpdateClientView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Clase de la vista de Modificacion de Cliente
    """
    template_name = 'clientes/cliente.html'
    model = Cliente
    form_class = UpdateClientForm
    success_url = './'
    success_message = 'Los cambios se guardaron correctamente'

    def get(self,request,*args,**kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        permisos = request.user.get_nombres_permisos()
        return self.render_to_response(self.get_context_data(permisos=permisos, form=form))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Cliente"
        context['direccion'] = {}
        context['direccion']['Clientes'] = (1, '/clientes/')
        context['direccion']['Modificar: ' + self.object.nombre] = (2, '/clientes/modificar/' + str(self.object.pk) + '/')
        return context

    def get_object(self, queryset=None):
        """
        Metodo que retorna el objeto a ser modificado
        :param queryset:
        :return: Retorna el cliente a ser modificado
        """
        return Cliente.objects.get(pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        """
        Metodo que es ejecutado al darse una consulta POST
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta POST
        """
        self.object = None
        formclass = self.get_form_class()
        form = self.get_form(formclass)
        permisos = request.user.get_nombres_permisos()
        if form.is_valid():
            self.object = form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(permisos=permisos,form=form))



@method_decorator(login_required, name='dispatch')
class VerClientDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    """
    Clase de la vista para ver clientes
    """
    model = Cliente
    template_name = 'clientes/ver_cliente.html'

    def get(self, request, *args, **kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object = self.get_object()
        permisos = request.user.get_nombres_permisos()
        return self.render_to_response(self.get_context_data(permisos=permisos))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super().get_context_data(**kwargs)
        context['title'] = "Ver Cliente"
        context['direccion'] = {}
        context['direccion']['Clientes'] = (1, '/clientes/')
        context['direccion']['Ver: ' + self.object.nombre] = (2, '/clientes/ver/' + str(self.object.pk) + '/')
        return context

    def get_object(self, queryset=None):
        """
        Metodo que retorna el objeto a ser visualizado
        :param queryset:
        :return: Retorna el cliente a ser visualizado
        """
        return Cliente.objects.get(pk=self.kwargs['pk'])