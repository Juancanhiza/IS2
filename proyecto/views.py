from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from .models import Proyecto
from .forms import ProyectoForm
"""
Vista del Login
"""
def listar_proyectos(request):
    lista = Proyecto.objects.order_by('id_proyecto')[:10]
    context = {'lista': lista}
    return render(request, '../templates/proyecto/listarProyecto.html', context)

def crear_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            Proyecto = form.save(commit=False)
            Proyecto.save()
            return redirect('proyectos:listar-proyectos')
    else:
        form = ProyectoForm()
    context = {'form': form}
    return render(request, '../templates/proyecto/crearProyecto.html', context)

def consultar_proyecto(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, pk=id_proyecto)
    context = {'proyecto': proyecto}
    return render(request, '../templates/proyecto/consultarProyecto.html', context)

def modificar_proyecto(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, pk=id_proyecto)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.save()
            return redirect('proyectos:listar-proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    context = {'form': form}
    return render(request, '../templates/proyecto/modificarProyecto.html', context)
