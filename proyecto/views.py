from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import *
from .forms import *
from proyecto.forms import CreateProjectForm, UpdateProjectForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden,HttpResponseRedirect
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


@method_decorator(login_required, name='dispatch')
class CreateProjectView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'proyecto/proyecto.html'
    model = Proyecto
    success_url = '/proyectos/'
    form_class = CreateProjectForm
    success_message = 'Se ha creado el proyecto'

    def get(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        proyectodetalle_orden_formset = ProyectoDetalleFormSet()
        return self.render_to_response(self.get_context_data(form=form, proyectodetalles=proyectodetalle_orden_formset))

    def get_context_data(self, **kwargs):
        context = super(CreateProjectView,self).get_context_data(**kwargs)
        context['title'] = "Crear Proyecto"
        return context

    def post(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form()
        proyectodetalle_formset = ProyectoDetalleFormSet(request.POST)

        if form.is_valid() and proyectodetalle_formset.is_valid():
            return self.form_valid(form,proyectodetalle_formset)
        else:
            return self.form_invalid(form,proyectodetalle_formset)

    def form_valid(self, form, proyectodetalle_formset):
        self.object = form.save()
        proyectodetalle_formset.instance = self.object
        proyectodetalle_formset.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form,proyectodetalle_formset):
        return self.render_to_respose(self.get_context_data(form=form,proyectodetalles=proyectodetalle_formset))




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
        detalles = ProyectoDetalle.objects.filter(proyecto=self.object).order_by('pk')
        detalles_data = []
        for detalle in detalles:
            d = {'usuario': detalle.usuario,
                 'rol': detalle.rol}
            detalles_data.append(d)
        ProyectoDetalleFormSet = inlineformset_factory(Proyecto, ProyectoDetalle, form=ProyectoDetalleForm,extra=len(detalles_data))
        proyectodetalle_orden_formset = ProyectoDetalleFormSet(initial=detalles_data)
        return self.render_to_response(self.get_context_data(form=form, proyectodetalles=proyectodetalle_orden_formset))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Proyecto"
        return context

    def get_object(self, queryset=None):
        return Proyecto.objects.get(pk=self.kwargs['pk'])

    def get_absolute_url(self):
        return reverse('update_rol', kwargs={'pk': self.kwargs['pk']})

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        proyectodetalle_formset = ProyectoDetalleFormSet(request.POST)
        if form.is_valid() and proyectodetalle_formset.is_valid():
            return self.form_valid(form,proyectodetalle_formset)
        else:
            return self.form_invalid(form,proyectodetalle_formset)

    def form_valid(self, form, proyectodetalle_formset):
        self.object = form.save()
        proyectodetalle_formset.instance = self.object
        ProyectoDetalle.objects.filter(proyecto=self.object).delete()
        proyectodetalle_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form,proyectodetalle_formset):
        return self.render_to_response(self.get_context_data(form=form, proyectodetalles=proyectodetalle_formset))

