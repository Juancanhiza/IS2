from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import UserStory
from userstory.forms import CreateUserStoryForm, UpdateUserStoryForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from tipoUserStory.models import *
from userstory.models import *


@method_decorator(login_required, name='dispatch')
class UserStoryListView(LoginRequiredMixin, ListView):
    """
    Vista de la lista de UserStory
    """
    template_name = 'userstory/list.html'
    model = UserStory
    queryset = UserStory.objects.all()

    def get(self,request,*args,**kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object = None
        self.object_list = UserStory.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(project=proyecto,object_list=self.object_list,permisos=permisos))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super(UserStoryListView,self).get_context_data(**kwargs)
        context['title'] = 'User Stories'
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['direccion'] = {}
        context['direccion']['Ejecuciones'] = (1, '/proyectos/ejecuciones/')
        context['direccion'][proyecto.nombre] = (2, '/proyectos/ejecuciones/' + str(proyecto.pk) + '/')
        context['direccion']['User Stories'] = (3, '/proyectos/ejecuciones/' + str(proyecto.pk) + '/userstories/')
        return context


@method_decorator(login_required, name='dispatch')
class CreateUserStoryView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Vista para la creacion de un User Story
    """
    template_name = 'userstory/userstory.html'
    model = UserStory
    success_url = '../'
    form_class = CreateUserStoryForm
    success_message = 'Se ha creado el user story'

    def get_object(self, queryset=None):
        """
        metodo que retorna el objeto actual
        :param queryset:
        :return: el objeto actual
        """
        obj = UserStory()
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        obj.proyecto = proyecto
        return obj

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
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos, form=form))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super().get_context_data(**kwargs)
        context['project'] = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['tipos_us'] = TipoUserStory.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        context['flujos'] = {}
        for tipo in context['tipos_us']:
            if tipo.pk not in context['flujos'].keys():
                context['flujos'][tipo.pk] = tipo.flujos.all
        context['title'] = "Crear User Story"
        context['direccion'] = {}
        context['direccion']['Ejecuciones'] = (1, '/proyectos/ejecuciones/')
        context['direccion'][str(context['project'])] = (2, '/proyectos/ejecuciones/' + str(self.kwargs['pk_proyecto']) + '/')
        context['direccion']['User Stories'] = (3, '/proyectos/ejecuciones/' + str(self.kwargs['pk_proyecto']) + '/userstories/')
        context['direccion']['Crear'] = (4, '/proyectos/ejecuciones/' + str(self.kwargs['pk_proyecto']) + '/userstories/create/')
        return context


@method_decorator(login_required, name='dispatch')
class UpdateUserStoryView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Vista para la modificacion de un User Story
    """
    template_name = 'userstory/userstory.html'
    model = UserStory
    form_class = UpdateUserStoryForm
    success_url = '../'
    success_message = 'Los cambios se guardaron correctamente'

    def get(self, request, *args, **kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object = self.get_object()
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super().get_context_data(**kwargs)
        context['project'] = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['tipos_us'] = TipoUserStory.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        context['flujos'] = {}
        for tipo in context['tipos_us']:
            if tipo.pk not in context['flujos'].keys():
                context['flujos'][tipo.pk] = tipo.flujos.all
        context['title'] = "Modificar User Story"
        context['direccion'] = {}
        context['direccion']['Ejecuciones'] = (1, '/proyectos/ejecuciones/')
        context['direccion'][str(context['project'])] = (2, '/proyectos/ejecuciones/' + str(self.kwargs['pk_proyecto']) + '/')
        context['direccion']['User Stories'] = (3, '/proyectos/ejecuciones/' + str(self.kwargs['pk_proyecto']) + '/userstories/')
        context['direccion']['Modificar: ' + self.object.nombre] = (4, '/proyectos/ejecuciones/' + str(self.kwargs['pk_proyecto']) + '/userstories/modificar/' + str(self.object.pk) + '/')
        return context

    def get_object(self, queryset=None):
        """
        metodo que retorna el objeto actual
        :param queryset:
        :return: el objeto actual
        """
        return UserStory.objects.get(pk=self.kwargs['pk'])


@method_decorator(login_required, name='dispatch')
class VerUserStoryDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    """
    Clase de la vista para ver User Stories, sin opcion de modificar
    """
    model = UserStory
    template_name = 'userstory/ver_userstory.html'

    def get(self, request, *args, **kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object = self.get_object()
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super().get_context_data(**kwargs)
        context['project'] = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['title'] = "Ver User Story"
        context['direccion'] = {}
        context['direccion']['Ejecuciones'] = (1, '/proyectos/ejecuciones/')
        context['direccion'][str(context['project'])] = (2, '/proyectos/ejecuciones/' + str(self.kwargs['pk_proyecto']) + '/')
        context['direccion']['Sprints'] = (3, '/proyectos/ejecuciones/' + str(self.kwargs['pk_proyecto']) + '/userstories/')
        context['direccion']['Ver: ' + self.object.nombre] = (4, '/proyectos/ejecuciones/' + str(self.kwargs['pk_proyecto']) + '/userstories/ver/' + str(self.object.pk) + '/')
        return context

    def get_object(self, queryset=None):
        """
        retorna el objecto actual
        :param queryset:
        :return: el objeto actual
        """
        return UserStory.objects.get(pk=self.kwargs['pk'])


@method_decorator(login_required, name='dispatch')
class ProductBacklogListView(LoginRequiredMixin, ListView):
    """
    Vista del Product Backlog
    """
    template_name = 'userstory/ProductBacklog.html'
    model = UserStory

    def get(self, request, *args, **kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object = None
        self.object_list = UserStory.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        ol = []
        for us in self.object_list:
            ol.append(us)
        ol.sort(key=lambda x: x.priorizacion, reverse=True)
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos, project=proyecto, ol=ol))


    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super(ProductBacklogListView,self).get_context_data(**kwargs)
        context['title'] = "Product Backlog"
        context['notas'] = {}
        context['archivos'] = {}
        context['actividades'] = {}
        for us in self.object_list:
            context['notas'][us.pk] = Nota.objects.filter(us=us.pk)
            context['archivos'][us.pk] = Archivo.objects.filter(us=us.pk)
            context['actividades'][us.pk] = Actividad.objects.filter(us=us.pk)
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['direccion'] = {}
        context['direccion']['Ejecuciones'] = (1, '/proyectos/ejecuciones/')
        context['direccion'][proyecto.nombre] = (2, '/proyectos/ejecuciones/' + str(proyecto.pk) + '/')
        context['direccion']['Product Backlog'] = (3, '/proyectos/ejecuciones/' + str(proyecto.pk) + '/productbacklog/')
        return context