from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Cliente
from .forms import ClienteForm
# Create your views here.

class ClientesView(ListView):
    template_name = 'clientes/AdminCliente.html'
    model = Cliente

def AgregarCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente = form.save(commit=False)
            Cliente.save()
            return redirect('clientes:ListarCliente')
    else:
        form = ClienteForm()
    context = {'form': form}
    return render(request, 'clientes/AgregarCliente.html', context)

def ListarClientes(request):
    lista = Cliente.objects.all()
    contex={'lista':lista}
    return render(request, 'clientes/ListarClientes.html', contex)

def ModificarCliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('clientes:ListarCliente')

    else:
        form = ClienteForm(instance=cliente)

    context = {'form': form}
    return render(request,'clientes/ModificarCliente.html', context)

def VerCliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    context = {'cliente': cliente}
    return render(request, 'clientes/VerCliente.html', context)