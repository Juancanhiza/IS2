from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from sprint.models import *
from userstory.forms import *
from proyecto.models import TeamMember
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


@method_decorator(login_required, name='dispatch')
class FlujoListView(LoginRequiredMixin, ListView):
    """
    Vista de la lista de Flujos
    """
    template_name = 'flujo/list.html'
    model = Flujo
    queryset = Flujo.objects.all()

    def get(self,request,*args,**kwargs):
        self.object = None
        self.object_list = Flujo.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos, project=proyecto,object_list=self.object_list))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Flujos de Proyecto"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateFlujoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Vista para la modificacion de flujo
    """
    template_name = 'flujo/flujo.html'
    model = Flujo
    success_url = '../'
    form_class = UpdateFlujoForm
    success_message = 'Se ha modificado el flujo'

    def get(self,request,*args,**kwargs):
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
        context = super().get_context_data(**kwargs)
        context['project'] = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['title'] = "Modificar Flujo " + str(self.object.pk)
        return context

    def get_object(self, queryset=None):
        return Flujo.objects.get(pk=self.kwargs['pk'])

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fases_formset = FaseFormSet(request.POST)
        if form.is_valid() and fases_formset.is_valid():
            return self.form_valid(form, fases_formset)
        else:
            return self.form_invalid(form, fases_formset)

    def form_valid(self, form, fases_formset):
        self.object = form.save()
        fases_formset.instance = self.object
        Fase.objects.filter(flujo=self.object).delete()
        fases_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form,fases_formset):
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
    success_url = '../'
    form_class = CreateFlujoForm
    success_message = 'Se ha creado el flujo'

    def get_object(self, queryset=None):
        obj = Flujo()
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        obj.proyecto = proyecto
        return obj

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fases_orden_formset = FaseFormSet()
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos, form=form, fases=fases_orden_formset))

    def get_context_data(self, **kwargs):
        context = super(CreateFlujoView,self).get_context_data(**kwargs)
        context['project'] = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        context['title'] = "Crear Flujo"
        return context

    def post(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fases_formset = FaseFormSet(request.POST)
        if form.is_valid() and fases_formset.is_valid():
            return self.form_valid(form,fases_formset)
        else:
            return self.form_invalid(form,fases_formset)

    def form_valid(self, form, fases_formset):
        self.object = form.save()
        fases_formset.instance = self.object
        fases_formset.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form,fases_formset):
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
        self.object = None
        usuario = request.user
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(usuario=usuario, permisos=permisos))

    def get_context_data(self, **kwargs):
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
            context['actividades'][us.pk] = Actividad.objects.filter(us=us.pk)
        context['direccion']['Ejecuciones'] = (1,"/proyectos/ejecuciones/")
        context['direccion']['Ejecucion '+str(context['project'].nombre)] = (2,"/proyectos/ejecuciones/"+str(self.kwargs['pk_proyecto'])+"/")
        link = "/proyectos/ejecuciones/"+str(self.kwargs['pk_proyecto'])+"/"
        link += "sprint/"+str(self.kwargs['sprint_pk'])+"/tableros/"
        link += str(self.kwargs['flujo_pk'])
        context['direccion']['Tablero ' + str(context['flujo'].nombre)] = (3,link)
        print(context['direccion'])
        return context

    def post(self, request, *args, **kwargs):
        """
        En este metodo se guardan los archivos, actividades o notas si lo que se agrega
        es un adjunto, o se mueve un US al estado siguiente o estado anterior o se mueve el
        US a una fase especifica si no paso el control de calidad o pasa a finalizado si es
        que paso el control de calidad, se toma una y solo una de las acciones mecionadas
        segun la consulta POST recibida
        """
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
                # Notificación al SCRUM por correo
                for member in TeamMember.objects.filter(proyecto=us.proyecto):
                    if member.rol.nombre == 'Scrum Master':
                        scrum_mail = member.usuario.email
                        scrum_nombre = member.usuario.first_name
                        break
                body = render_to_string(
                    '../templates/notificaciones/cambio_estado.html', {
                        # Poner los parámetros requeridos del correo
                        'nombre_scrum': scrum_nombre,
                        'nombre_us': us.nombre,
                        'proyecto': us.proyecto.nombre,
                        'sprint': us.sprint.nombre,
                        'estado_actual': 'To Do',
                        'estado_nuevo': us.estado_fase,
                        'team_member': us.team_member,
                        'fase': us.fase.nombre,
                        'horas_restantes': us.duracion_estimada,  # ESTE DEBE SER LA DURACIÓN REAL
                    },
                )
                email_msg = EmailMessage(
                    subject='Cambio de Estado US',
                    body=body,
                    from_email=['PoliProyectos-noreply'],
                    to=[scrum_mail],
                )
                email_msg.content_subtype = 'html'
                email_msg.send()

            elif us.estado_fase == 'Doing':
                us.estado_fase = "Done"
                us.save()
                # Notificación al SCRUM por correo
                for member in TeamMember.objects.filter(proyecto=us.proyecto):
                    if member.rol.nombre == 'Scrum Master':
                        scrum_mail = member.usuario.email
                        scrum_nombre = member.usuario.first_name
                        break
                body = render_to_string(
                    '../templates/notificaciones/cambio_estado.html', {
                        # Poner los parámetros requeridos del correo
                        'nombre_scrum': scrum_nombre,
                        'nombre_us': us.nombre,
                        'proyecto': us.proyecto.nombre,
                        'sprint': us.sprint.nombre,
                        'fase': us.fase.nombre,
                        'estado_actual': 'Doing',
                        'estado_nuevo': us.estado_fase,
                        'team_member': us.team_member,
                        'horas_restantes': us.duracion_estimada,  # ESTE DEBE SER LA DURACIÓN REAL
                    },
                )
                email_msg = EmailMessage(
                    subject='Cambio de Estado US',
                    body=body,
                    from_email=['PoliProyectos-noreply'],
                    to=[scrum_mail],
                )
                email_msg.content_subtype = 'html'
                email_msg.send()
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
                    # Notificación al SCRUM por correo
                    for member in TeamMember.objects.filter(proyecto=us.proyecto):
                        if member.rol.nombre == 'Scrum Master':
                            scrum_mail = member.usuario.email
                            scrum_nombre = member.usuario.first_name
                            break
                    body = render_to_string(
                        '../templates/notificaciones/cambio_fase.html', {
                            # Poner los parámetros requeridos del correo
                            'nombre_scrum': scrum_nombre,
                            'nombre_us': us.nombre,
                            'proyecto': us.proyecto.nombre,
                            'sprint': us.sprint.nombre,
                            'team_member': us.team_member,
                            'fase_actual': fases[idx_fase].nombre,
                            'fase_nueva': us.fase.nombre,
                            'horas_restantes': us.duracion_estimada,  # ESTE DEBE SER LA DURACIÓN REAL
                        },
                    )
                    email_msg = EmailMessage(
                        subject='Cambio de Fase US',
                        body=body,
                        from_email=['PoliProyectos-noreply'],
                        to=[scrum_mail],
                    )
                    email_msg.content_subtype = 'html'
                    email_msg.send()
                else: #es la ultima fase, pasa a control de calidad
                    us.fase = None
                    us.estado_fase = 'Control de Calidad'
                    # Notificación al SCRUM por correo
                    for member in TeamMember.objects.filter(proyecto=us.proyecto):
                        if member.rol.nombre == 'Scrum Master':
                            scrum_mail = member.usuario.email
                            scrum_nombre = member.usuario.first_name
                            break
                    body = render_to_string(
                        '../templates/notificaciones/control_de_calidad.html', {
                            # Poner los parámetros requeridos del correo
                            'nombre_scrum': scrum_nombre,
                            'nombre_us': us.nombre,
                            'proyecto': us.proyecto.nombre,
                            'sprint': us.sprint.nombre,
                            'team_member': us.team_member,
                            'horas_restantes': us.duracion_estimada,  # ESTE DEBE SER LA DURACIÓN REAL
                        },
                    )
                    email_msg = EmailMessage(
                        subject='US para Control de Calidad',
                        body=body,
                        from_email=['PoliProyectos-noreply'],
                        to=[scrum_mail],
                    )
                    email_msg.content_subtype = 'html'
                    email_msg.send()
                us.save()
        if 'anterior' in request.POST.keys():
            us = UserStory.objects.get(id=request.POST['anterior'])
            if us.estado_fase == 'Done':
                us.estado_fase = 'Doing'
                us.save()
                # Notificación al SCRUM por correo
                for member in TeamMember.objects.filter(proyecto=us.proyecto):
                    if member.rol.nombre == 'Scrum Master':
                        scrum_mail = member.usuario.email
                        scrum_nombre = member.usuario.first_name
                        break
                body = render_to_string(
                    '../templates/notificaciones/cambio_estado.html', {
                        # Poner los parámetros requeridos del correo
                        'nombre_scrum': scrum_nombre,
                        'nombre_us': us.nombre,
                        'proyecto': us.proyecto.nombre,
                        'sprint': us.sprint.nombre,
                        'estado_actual': 'Done',
                        'estado_nuevo': us.estado_fase,
                        'team_member': us.team_member,
                        'fase': us.fase.nombre,
                        'horas_restantes': us.duracion_estimada,  # ESTE DEBE SER LA DURACIÓN REAL
                    },
                )
                email_msg = EmailMessage(
                    subject='Cambio de Estado US',
                    body=body,
                    from_email=['PoliProyectos-noreply'],
                    to=[scrum_mail],
                )
                email_msg.content_subtype = 'html'
                email_msg.send()
            elif us.estado_fase == 'Doing':
                us.estado_fase = "To Do"
                us.save()
                # Notificación al SCRUM por correo
                for member in TeamMember.objects.filter(proyecto=us.proyecto):
                    if member.rol.nombre == 'Scrum Master':
                        scrum_mail = member.usuario.email
                        scrum_nombre = member.usuario.first_name
                        break
                body = render_to_string(
                    '../templates/notificaciones/cambio_estado.html', {
                        # Poner los parámetros requeridos del correo
                        'nombre_scrum': scrum_nombre,
                        'nombre_us': us.nombre,
                        'proyecto': us.proyecto.nombre,
                        'sprint': us.sprint.nombre,
                        'estado_actual': 'Doing',
                        'estado_nuevo': us.estado_fase,
                        'team_member': us.team_member,
                        'fase': us.fase.nombre,
                        'horas_restantes': us.duracion_estimada,  # ESTE DEBE SER LA DURACIÓN REAL
                    },
                )
                email_msg = EmailMessage(
                    subject='Cambio de Estado US',
                    body=body,
                    from_email=['PoliProyectos-noreply'],
                    to=[scrum_mail],
                )
                email_msg.content_subtype = 'html'
                email_msg.send()
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
                # Notificación al SCRUM por correo
                for member in TeamMember.objects.filter(proyecto=us.proyecto):
                    if member.rol.nombre == 'Scrum Master':
                        scrum_mail = member.usuario.email
                        scrum_nombre = member.usuario.first_name
                        break
                body = render_to_string(
                    '../templates/notificaciones/cambio_fase.html', {
                        # Poner los parámetros requeridos del correo
                        'nombre_scrum': scrum_nombre,
                        'nombre_us': us.nombre,
                        'proyecto': us.proyecto.nombre,
                        'sprint': us.sprint.nombre,
                        'team_member': us.team_member,
                        'fase_actual': fases[idx_fase].nombre,
                        'fase_nueva': us.fase.nombre,
                        'horas_restantes': us.duracion_estimada,  # ESTE DEBE SER LA DURACIÓN REAL
                    },
                )
                email_msg = EmailMessage(
                    subject='Cambio de Fase US',
                    body=body,
                    from_email=['PoliProyectos-noreply'],
                    to=[scrum_mail],
                )
                email_msg.content_subtype = 'html'
                email_msg.send()
        if 'finalizar' in request.POST.keys():
            us = UserStory.objects.get(id=request.POST['finalizar'])
            us.fase = None
            us.estado_fase = 'Done'
            us.estado = 0
            us.save()
            # Notificación al Desarrollador por correo
            body = render_to_string(
                '../templates/notificaciones/control_calidad_aceptado.html', {
                    # Poner los parámetros requeridos del correo
                    'nombre_us': us.nombre,
                    'proyecto': us.proyecto.nombre,
                    'sprint': us.sprint.nombre,
                    'team_member': us.team_member.first_name,
                },
            )
            email_msg = EmailMessage(
                subject='QA: Finalización Aprobada de US',
                body=body,
                from_email=['PoliProyectos-noreply'],
                to=[us.team_member.email],
            )
            email_msg.content_subtype = 'html'
            email_msg.send()
        if 'fase' in request.POST.keys():
            us = UserStory.objects.get(id=request.POST['us'])
            fase = Fase.objects.get(id=request.POST['fase'])
            us.fase = fase
            us.estado_fase = 'To Do'
            us.save()
            # Notificación al Desarrollador por correo
            body = render_to_string(
                '../templates/notificaciones/control_calidad_rechazado.html', {
                    # Poner los parámetros requeridos del correo
                    'nombre_us': us.nombre,
                    'proyecto': us.proyecto.nombre,
                    'sprint': us.sprint.nombre,
                    'team_member': us.team_member.first_name,
                    'fase_nueva': us.fase.nombre,
                },
            )
            email_msg = EmailMessage(
                subject='QA: Se necesitan realizar modificaciones a US',
                body=body,
                from_email=['PoliProyectos-noreply'],
                to=[us.team_member.email],
            )
            email_msg.content_subtype = 'html'
            email_msg.send()
        return HttpResponseRedirect('./')

@method_decorator(login_required, name='dispatch')
class VerFlujoDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Flujo
    template_name = 'flujo/ver_flujo.html'

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        permisos = request.user.get_nombres_permisos(proyecto=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(permisos=permisos))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ver Flujo " + str(self.object.pk)
        return context

    def get_object(self, queryset=None):
        return Flujo.objects.get(pk=self.kwargs['pk'])