from django.urls import path
from django.conf.urls import url
from . import views
# from django.contrib.auth.views import login

"""
Definicion de URLs contenidas en clientes
"""

urlpatterns = [
	url(r'^$', views.ListarClientes, name='ListarCliente'),
	url(r'^AgregarCliente', views.AgregarCliente, name='AgregarCliente'),
	path('<int:id_cliente>/ModificarCliente/',views.ModificarCliente,name='ModificarCliente'),
	path('<int:id_cliente>/VerCliente/', views.VerCliente, name='VerCliente'),
]