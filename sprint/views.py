from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.http import HttpResponseRedirect
from .models import Sprint
from proyecto.models import Proyecto
from sprint.forms import CreateSprintForm, UpdateSprintForm
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from userstory.models import UserStory
from flujo.models import *
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
    success_url = '../'
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
    success_url = '../'
    success_message = 'Los cambios se guardaron correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Sprint"
        return context

    def get_object(self, queryset=None):
        return Sprint.objects.get(pk=self.kwargs['sprint_pk'])

    def get_absolute_url(self):
        return reverse('update_sprint', kwargs={'sprint_pk': self.kwargs['sprint_pk']})


@method_decorator(login_required, name='dispatch')
class AsignarUSUpdateView(LoginRequiredMixin, ListView):
    template_name = 'sprint/asignar_us.html'
    model = UserStory

    def get(self,request,*args,**kwargs):
        self.object = None
        self.object_list = UserStory.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        sprint = Sprint.objects.get(pk=self.kwargs['sprint_pk'])
        return self.render_to_response(self.get_context_data(sprint=sprint,project=proyecto, object_list=self.object_list))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AsignarUSUpdateView,self).get_context_data(**kwargs)
        context["title"] = "Asignar User Stories"
        return context

    def post(self,request,*args,**kwargs):
        self.object = None
        sprint = Sprint.objects.get(pk=self.kwargs['sprint_pk'])
        try:
            user_stories = request.POST.getlist('user_stories')
        except:
            user_stories = []
        last_user_stories = UserStory.objects.filter(proyecto=self.kwargs['pk_proyecto'],sprint=sprint.pk)
        '''Se quita la asignacion a todos los us que estaban asignados al sprint antes'''
        for us in last_user_stories:
            us.sprint = None
            us.save()
        '''Se asignan los us al sprint'''
        for us_id in user_stories:
            us = UserStory.objects.get(pk=us_id)
            us.sprint = sprint
            us.save()
        return HttpResponseRedirect('../../')
