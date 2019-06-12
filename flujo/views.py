from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from sprint.models import *
from userstory.forms import *
from django.shortcuts import render


@method_decorator(login_required, name='dispatch')
class FlujoListView(LoginRequiredMixin, ListView):
    """
    Clase de la vista de la lista de Flujos
    """
    template_name = 'flujo/list.html'
    model = Flujo
    queryset = Flujo.objects.all()

    def get(self,request,*args,**kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object = None
        self.object_list = Flujo.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos, project=proyecto,object_list=self.object_list))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super().get_context_data(**kwargs)
        context['title'] = "Flujos de Proyecto"
        context['direccion'] = {}
        context['direccion']['Definiciones'] = (1, '/proyectos/definiciones/')
        context['direccion'][str(kwargs['project'])] = (2, '/proyectos/definiciones/'+str(kwargs['project'].pk)+'/')
        context['direccion']['Flujos'] = (3, '/proyectos/definiciones/'+str(kwargs['project'].pk)+'/flujos/')
        return context


@method_decorator(login_required, name='dispatch')
class UpdateFlujoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Vista para la modificacion de flujo
    """
    template_name = 'flujo/flujo.html'
    model = Flujo
    success_url = '../../'
    form_class = UpdateFlujoForm
    success_message = 'Se ha modificado el flujo'

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
        fases = Fase.objects.filter(flujo=self.object).order_by('pk')
        fases_data = []
        for fase in fases:
            d = {'nombre': fase.nombre,}
            fases_data.append(d)
        FaseFormSet = inlineformset_factory(Flujo, Fase, form=FaseForm,extra=len(fases_data))
        fases_orden_formset = FaseFormSet(initial=fases_data)
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos,form=form, fases=fases_orden_formset))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super().get_context_data(**kwargs)
        context['project'] = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['title'] = "Modificar Flujo " + str(self.object.pk)
        context['direccion'] = {}
        context['direccion']['Definiciones'] = (1, '/proyectos/definiciones/')
        context['direccion'][str(context['project'])] = (2, '/proyectos/definiciones/' + str(self.kwargs['pk_proyecto']) + '/')
        context['direccion']['Flujos'] = (3, '/proyectos/definiciones/' + str(self.kwargs['pk_proyecto']) + '/flujos/')
        context['direccion']['Modificar:'+self.object.nombre] = (4, '/proyectos/definiciones/' + str(self.kwargs['pk_proyecto']) + '/flujos/modificar/' + str(self.object.pk))
        return context

    def get_object(self, queryset=None):
        """
        Metodo que retorna el objeto a ser modificado
        :param queryset:
        :return: El proyecto a ser modificado
        """
        return Flujo.objects.get(pk=self.kwargs['pk'])

    def post(self,request,*args,**kwargs):
        """
        Metodo que es ejecutado al darse una consulta POST
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta POST
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fases_formset = FaseFormSet(request.POST)
        if form.is_valid() and fases_formset.is_valid():
            return self.form_valid(form, fases_formset)
        else:
            return self.form_invalid(form, fases_formset)

    def form_valid(self, form, fases_formset):
        """
        Metodo que se ejecuta si el formulario recibido en la consulta POST
        es valido
        :param form: formulario a ser guardado
        :param team_member_formset: grupo de team members del proyecto
        :return: redireccion a la direccion definida en el atributo success_url de la clase
        """
        self.object = form.save()
        fases_formset.instance = self.object
        Fase.objects.filter(flujo=self.object).delete()
        fases_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form,fases_formset):
        """
        Metodo que se ejecuta si el formulario recibido en la consulta POST
        es invalido
        :param form: formulario a ser guardado
        :param team_member_formset: grupo de team members del proyecto
        :return: redireccion a la pagina actual con los errores de validacion
        """
        fs_error = None
        if fases_formset.vacio:
            fs_error = "El flujo debe tener al menos una fase"
        if fases_formset.sin_nombre:
            fs_error = "Las fases deben tener un nombre"
        return self.render_to_response(self.get_context_data(fs_error=fs_error, form=form, fases=fases_formset))


@method_decorator(login_required, name='dispatch')
class CreateFlujoView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Vista de la creacion de Flujo
    """
    template_name = 'flujo/flujo.html'
    model = Flujo
    success_url = '../../'
    form_class = CreateFlujoForm
    success_message = 'Se ha creado el flujo'

    def get_object(self, queryset=None):
        """
        Metodo que retorna el objeto a ser visualizado
        :param queryset:
        :return: Retorna el proyecto a ser visualizado
        """
        obj = Flujo()
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
        fases_orden_formset = FaseFormSet()
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos, form=form, fases=fases_orden_formset))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super(CreateFlujoView,self).get_context_data(**kwargs)
        context['project'] = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['title'] = "Crear Flujo"
        context['direccion'] = {}
        context['direccion']['Definiciones'] = (1, '/proyectos/definiciones/')
        context['direccion'][str(context['project'])] = (2, '/proyectos/definiciones/' + str(self.kwargs['pk_proyecto']) + '/')
        context['direccion']['Flujos'] = (3, '/proyectos/definiciones/' + str(self.kwargs['pk_proyecto']) + '/flujos/')
        context['direccion']['Crear'] = (4, '/proyectos/definiciones/' + str(self.kwargs['pk_proyecto']) + '/flujos/create/')
        return context

    def post(self,request,*args,**kwargs):
        """
        Metodo que es ejecutado al darse una consulta POST
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta POST
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fases_formset = FaseFormSet(request.POST)
        if form.is_valid() and fases_formset.is_valid():
            return self.form_valid(form,fases_formset)
        else:
            return self.form_invalid(form,fases_formset)

    def form_valid(self, form, fases_formset):
        """
        Metodo que se ejecuta si el formulario recibido en la consulta POST
        es valido
        :param form: formulario a ser guardado
        :param team_member_formset: grupo de team members del proyecto
        :return: redireccion a la direccion definida en el atributo success_url de la clase
        """
        self.object = form.save()
        fases_formset.instance = self.object
        fases_formset.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form,fases_formset):
        """
        Metodo que se ejecuta si el formulario recibido en la consulta POST
        es invalido
        :param form: formulario a ser guardado
        :param team_member_formset: grupo de team members del proyecto
        :return: redireccion a la pagina actual con los errores de validacion
        """
        fs_error = None
        if fases_formset.vacio:
            fs_error = "El flujo debe tener al menos una fase"
        if fases_formset.sin_nombre:
            fs_error = "Las fases deben tener un nombre"
        return self.render_to_response(self.get_context_data(fs_error=fs_error, form=form, fases=fases_formset))


@method_decorator(login_required, name='dispatch')
class TableroTemplateView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    """
    Vista del tablero de los flujos
    """
    template_name = 'flujo/tablero.html'

    def get(self,request,*args,**kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object = None
        usuario = request.user
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(usuario=usuario, permisos=permisos))

    def get_context_data(self, **kwargs):
        """
        Metodo que retorna un diccionario utilizado para pasar datos a las vistas
        :param kwargs: Diccionario de datos adicionales para el contexto
        :return: diccionario de contexto necesario para la correcta visualizacion de los datos
        """
        context = super(TableroTemplateView, self).get_context_data(**kwargs)
        context['title'] = "Tableros de Proyecto"
        context['project'] = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['sprint_actual'] = Sprint.objects.get(pk=self.kwargs['sprint_pk'])
        context['flujo'] = Flujo.objects.get(pk=self.kwargs['flujo_pk'])
        context['fases'] = Fase.objects.filter(flujo=self.kwargs['flujo_pk']).order_by('pk')
        context['user_stories'] = UserStory.objects.filter(sprint=self.kwargs['sprint_pk'])
        context['nota_form'] = NotaForm()
        context['archivo_form'] = ArchivoForm()
        context['actividad_form'] = ActividadForm()
        context['notas'] = {}
        context['archivos'] = {}
        context['direccion'] = {}
        context['actividades'] = {}
        for us in context['user_stories']:
            context['notas'][us.pk] = Nota.objects.filter(us=us.pk)
            context['archivos'][us.pk] = Archivo.objects.filter(us=us.pk)
            actividades = Actividad.objects.filter(us=us.pk)
            cambios = CambioEstado.objects.filter(us=us.pk)
            context['actividades'][us.pk] = []
            for a in actividades:
                a.tipo = 'actividad'
                context['actividades'][us.pk].append(a)
            for c in cambios:
                c.tipo = 'cambio'
                context['actividades'][us.pk].append(c)
            context['actividades'][us.pk].sort(key=lambda x: x.fecha, reverse=True)
        context['direccion']['Ejecuciones'] = (1,"/proyectos/ejecuciones/")
        context['direccion'][str(context['project'].nombre)] = (2,"/proyectos/ejecuciones/"+str(self.kwargs['pk_proyecto'])+"/")
        link = "/proyectos/ejecuciones/"+str(self.kwargs['pk_proyecto'])+"/"
        link += "sprint/"+str(self.kwargs['sprint_pk'])+"/tableros/"
        link += str(self.kwargs['flujo_pk'])
        context['direccion']['Tablero ' + str(context['flujo'].nombre)] = (3,link)
        return context

    def post(self, request, *args, **kwargs):
        """
        En este metodo se guardan los archivos, actividades o notas si lo que se agrega
        es un adjunto, o se mueve un US al estado siguiente o estado anterior o se mueve el
        US a una fase especifica si no paso el control de calidad o pasa a finalizado si es
        que paso el control de calidad, se toma una y solo una de las acciones mecionadas
        segun la consulta POST recibida
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta POST
        """
        usuario = request.user
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        if 'tipo-adjunto' in request.POST.keys():
            if request.POST['tipo-adjunto'] == 'nota':
                adjunto = GuardarNotaForm(request.POST)
            if request.POST['tipo-adjunto'] == 'archivo':
                adjunto = GuardarArchivoForm(request.POST, request.FILES)
            if request.POST['tipo-adjunto'] == 'actividad':
                adjunto = GuardarActividadForm(request.POST)
            if adjunto.is_valid():
                adjunto.save()
            else:
                self.render_to_response(self.get_context_data(formulario=adjunto))
        elif 'siguiente' in request.POST.keys():
            us = UserStory.objects.get(id=request.POST['siguiente'])
            if us.estado_fase == 'To Do':
                us.estado_fase = 'Doing'
                us.save()
            elif us.estado_fase == 'Doing':
                ultima_actividad = list(Actividad.objects.filter(us=us.pk,sprint=us.sprint).order_by('fecha').reverse())
                ultimo_cambio = list(CambioEstado.objects.filter(us=us.pk,sprint=us.sprint).order_by('fecha').reverse())
                if ultima_actividad and ultimo_cambio:
                    ultima_actividad = ultima_actividad[0]
                    ultimo_cambio = ultimo_cambio[0]
                    if ultima_actividad.fecha < ultimo_cambio.fecha:
                        return self.render_to_response(self.get_context_data(s_fase=us.fase,usuario=usuario,
                                                                             permisos=permisos, error='sinactividad'))
                else:
                    return self.render_to_response(self.get_context_data(s_fase=us.fase, usuario=usuario,
                                                                         permisos=permisos, error='sinactividad'))
                us.estado_fase = "Done"
                us.save()
            elif us.estado_fase == 'Done':
                fases = Fase.objects.filter(flujo=self.kwargs['flujo_pk']).order_by('pk')
                idx_fase = None
                pos = -1
                for f in fases:
                    pos += 1
                    if f == us.fase:
                        idx_fase = pos
                        break
                if idx_fase < len(fases) - 1: #no es la ultima fase
                    us.fase = fases[idx_fase + 1]
                    us.estado_fase = 'To Do'
                    us.save()
                else: #es la ultima fase, pasa a control de calidad
                    us.fase = None
                    us.estado_fase = 'Control de Calidad'
                us.save()
            ce = CambioEstado()
            ce.us = us
            ce.fase = us.fase
            ce.sprint = us.sprint
            ce.usuario = request.user
            ce.estado_fase = us.estado_fase
            ce.descripcion = "Cambio de estado a " + us.estado_fase + " de la fase " + us.fase.nombre
            ce.save()
            return render(request,'flujo/tablero.html',self.get_context_data(s_fase=us.fase,usuario=usuario, permisos=permisos))
        if 'anterior' in request.POST.keys():
            us = UserStory.objects.get(id=request.POST['anterior'])
            if us.estado_fase == 'Done':
                us.estado_fase = 'Doing'
                us.save()
            elif us.estado_fase == 'Doing':
                us.estado_fase = "To Do"
                us.save()
            elif us.estado_fase == 'To Do':
                fases = Fase.objects.filter(flujo=self.kwargs['flujo_pk']).order_by('pk')
                idx_fase = None
                pos = -1
                for f in fases:
                    pos += 1
                    if f == us.fase:
                        idx_fase = pos
                        break
                us.fase = fases[idx_fase - 1]
                us.estado_fase = 'To Do'
                us.save()
            ce = CambioEstado()
            ce.us = us
            ce.fase = us.fase
            ce.sprint = us.sprint
            ce.usuario = request.user
            ce.estado_fase = us.estado_fase
            ce.descripcion = "Cambio de estado a " + us.estado_fase + " de la fase " + us.fase.nombre
            ce.save()
            return render(request, 'flujo/tablero.html',
                          self.get_context_data(s_fase=us.fase, usuario=usuario, permisos=permisos))
        if 'finalizar' in request.POST.keys():
            us = UserStory.objects.get(id=request.POST['finalizar'])
            us.fase = None
            us.estado_fase = 'Done'
            us.estado = 0
            us.save()
        if 'fase' in request.POST.keys():
            us = UserStory.objects.get(id=request.POST['us'])
            fase = Fase.objects.get(id=request.POST['fase'])
            us.fase = fase
            us.estado_fase = 'To Do'
            us.save()
        return HttpResponseRedirect('./')

@method_decorator(login_required, name='dispatch')
class VerFlujoDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    """
    Vista para ver un flujo, sin opciones de modificación
    """
    model = Flujo
    template_name = 'flujo/ver_flujo.html'

    def get(self,request,*args,**kwargs):
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
        context['title'] = "Ver Flujo " + str(self.object.pk)
        context['direccion'] = {}
        context['direccion']['Definiciones'] = (1, '/proyectos/definiciones/')
        context['direccion'][str(context['project'])] = (2, '/proyectos/definiciones/' + str(self.kwargs['pk_proyecto']) + '/')
        context['direccion']['Flujos'] = (3, '/proyectos/definiciones/' + str(self.kwargs['pk_proyecto']) + '/flujos/')
        context['direccion']['Ver: ' + self.object.nombre] = (4, '/proyectos/definiciones/' + str(self.kwargs['pk_proyecto']) + '/flujos/ver/' + str(self.object.pk))
        return context

    def get_object(self, queryset=None):
        """
        Metodo que retorna el objeto a ser visualizado
        :param queryset:
        :return: El proyecto a ser modificado
        """
        return Flujo.objects.get(pk=self.kwargs['pk'])