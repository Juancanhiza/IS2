from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm

def list(request):
    lista = Usuario.objects.order_by('id_usuario')[:10]
    context = {'lista': lista}
    return render(request, '../templates/usuarios/list.html', context)

def add(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            Usuario= form.save(commit=False)
            Usuario.save()
            return redirect('usuarios:list')
    else:
        form = UsuarioForm()
    context = {'form': form}
    return render(request, '../templates/usuarios/add.html', context)

def modify(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect('usuarios:list')
    else:
        form = UsuarioForm(instance=usuario)
    context = {'form': form}
    return render(request, '../templates/usuarios/modify.html', context)

def query(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    context = {'usuario': usuario}
    return render(request, '../templates/usuarios/query.html', context)
