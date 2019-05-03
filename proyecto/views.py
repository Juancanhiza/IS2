from django.views.generic import ListView, CreateView, UpdateView
from .forms import *
from proyecto.forms import CreateProjectForm, UpdateProjectForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from sprint.models import *
from flujo.models import *

''' Vistas de proyecto'''

@method_decorator(login_required, name='dispatch')
class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'proyecto/list.html'
    model = Proyecto
    queryset = Proyecto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Administración de Proyectos"
        return context


@method_decorator(login_required, name='dispatch')
class CreateProjectView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'proyecto/proyecto.html'
    model = Proyecto
    success_url = '/proyectos/'
    form_class = CreateProjectForm
    success_message = 'Se ha creado el proyecto'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_member_formset = TeamMemberFormSet()
        return self.render_to_response(
            self.get_context_data(form=form, team_members=team_member_formset))

    def get_context_data(self, **kwargs):
        context = super(CreateProjectView, self).get_context_data(**kwargs)
        context['title'] = "Crear Proyecto"
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_member_formset = TeamMemberFormSet(request.POST)

        if form.is_valid() and team_member_formset.is_valid():
            return self.form_valid(form, team_member_formset)
        else:
            return self.form_invalid(form, team_member_formset)

    def form_valid(self, form, team_member_formset):
        self.object = form.save()
        team_member_formset.instance = self.object
        team_member_formset.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, team_member_formset):
        return self.render_to_respose(self.get_context_data(form=form, team_members=team_member_formset))


@method_decorator(login_required, name='dispatch')
class UpdateProjectView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'proyecto/proyecto.html'
    model = Proyecto
    form_class = UpdateProjectForm
    success_url = '/proyectos/'
    success_message = 'Los cambios se guardaron correctamente'

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_members = TeamMember.objects.filter(proyecto=self.object).order_by('pk')
        tm_data = []
        for tm in team_members:
            d = {'usuario': tm.usuario,
                 'rol': tm.rol}
            tm_data.append(d)
        TeamMemberFormSet = inlineformset_factory(Proyecto, TeamMember, form=TeamMemberForm, extra=len(tm_data))
        team_member_formset = TeamMemberFormSet(initial=tm_data)
        return self.render_to_response(self.get_context_data(form=form, team_members=team_member_formset))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Proyecto"
        return context

    def get_object(self, queryset=None):
        return Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])

    def get_absolute_url(self):
        return reverse('update_project', kwargs={'pk_proyecto': self.kwargs['pk_proyecto']})

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_member_formset = TeamMemberFormSet(request.POST)
        if form.is_valid() and team_member_formset.is_valid():
            return self.form_valid(form, team_member_formset)
        else:
            return self.form_invalid(form, team_member_formset)

    def form_valid(self, form, team_member_formset):
        self.object = form.save()
        team_member_formset.instance = self.object
        TeamMember.objects.filter(proyecto=self.object).delete()
        team_member_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, team_member_formset):
        return self.render_to_response(self.get_context_data(form=form, team_members=team_member_formset))


'''  Vistas de opciones de proyecto '''

@method_decorator(login_required, name='dispatch')
class OptionsListView(LoginRequiredMixin, ListView):
    template_name = 'proyecto/opciones_list.html'
    model = Proyecto
    queryset = Proyecto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Opciones de Proyectos"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateOptionsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'proyecto/options.html'
    model = Proyecto
    form_class = UpdateProjectForm
    success_url = '/proyectos/opciones/'
    success_message = 'Los cambios se guardaron correctamente'

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_members = TeamMember.objects.filter(proyecto=self.object).order_by('pk')
        tm_data = []
        for tm in team_members:
            d = {'usuario': tm.usuario,
                 'rol': tm.rol}
            tm_data.append(d)
        TeamMemberFormSet = inlineformset_factory(Proyecto, TeamMember, form=TeamMemberForm,extra=len(tm_data))
        team_member_formset = TeamMemberFormSet(initial=tm_data)
        return self.render_to_response(self.get_context_data(form=form, team_members=team_member_formset))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Proyecto"
        return context

    def get_object(self, queryset=None):
        return Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])

    def get_absolute_url(self):
        return reverse('update_options', kwargs={'pk_proyecto': self.kwargs['pk_proyecto']})

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_member_formset = TeamMemberFormSet(request.POST)
        if form.is_valid() and team_member_formset.is_valid():
            return self.form_valid(form, team_member_formset)
        else:
            return self.form_invalid(form, team_member_formset)

    def form_valid(self, form, team_member_formset):
        self.object = form.save()
        team_member_formset.instance = self.object
        TeamMember.objects.filter(proyecto=self.object).delete()
        team_member_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form,team_member_formset):
        return self.render_to_response(self.get_context_data(form=form, team_members=team_member_formset))


'''vistas de ejecucion'''


@method_decorator(login_required, name='dispatch')
class EjecucionListView(LoginRequiredMixin, ListView):
    template_name = 'proyecto/ejecuciones_list.html'
    model = Proyecto
    queryset = Proyecto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ejecuciones de Proyectos"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateEjecucionView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'proyecto/ejecucion.html'
    model = Proyecto
    form_class = UpdateProjectForm
    success_url = '/proyectos/ejecuciones/'
    success_message = 'Los cambios se guardaron correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ejecucion de Proyecto"
        try:
            context['sprint_pendiente'] = Sprint.objects.get(proyecto=self.kwargs['pk_proyecto'], estado="Pendiente")
        except:
            pass
        try:
            context['sprint_actual'] = Sprint.objects.get(proyecto=self.kwargs['pk_proyecto'], estado="En Proceso")
        except:
            pass
        flujos = Flujo.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        context['flujos'] = flujos
        context['project'] = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        return context

    def get_object(self, queryset=None):
        return Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])

    def get_absolute_url(self):
        return reverse('update_ejecucion', kwargs={'pk_proyecto': self.kwargs['pk_proyecto']})


@method_decorator(login_required, name='dispatch')
class UpdateTeamMemberView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'proyecto/asignacion_roles.html'
    model = Proyecto
    form_class = UpdateProjectForm
    success_url = '../'
    success_message = 'Los cambios se guardaron correctamente'

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_members = TeamMember.objects.filter(proyecto=self.object).order_by('pk')
        tm_data = []
        for tm in team_members:
            d = {'usuario': tm.usuario,
                 'rol': tm.rol}
            tm_data.append(d)
        TeamMemberFormSet = inlineformset_factory(Proyecto, TeamMember, form=TeamMemberForm,extra=len(tm_data))
        team_member_formset = TeamMemberFormSet(initial=tm_data)
        return self.render_to_response(self.get_context_data(form=form, team_members=team_member_formset))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Proyecto"
        return context

    def get_object(self, queryset=None):
        return Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])

    def get_absolute_url(self):
        return reverse('update_project', kwargs={'pk_proyecto': self.kwargs['pk_proyecto']})

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_member_formset = TeamMemberFormSet(request.POST)
        if form.is_valid() and team_member_formset.is_valid():
            return self.form_valid(form, team_member_formset)
        else:
            return self.form_invalid(form, team_member_formset)

    def form_valid(self, form, team_member_formset):
        self.object = form.save()
        team_member_formset.instance = self.object
        TeamMember.objects.filter(proyecto=self.object).delete()
        team_member_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, team_member_formset):
        return self.render_to_response(self.get_context_data(form=form, team_members=team_member_formset))