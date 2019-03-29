from django.conf.urls import url
from django.urls import path
from . import views

"""
URL para el login, y para cuando se loguea
"""
app_name = 'proyectos'
urlpatterns = [
	url(r'^$', views.listar_proyectos, name='listar-proyectos'),
	url(r'^crear-proyecto/', views.crear_proyecto, name='crear_proyecto'),
	path('<int:id_proyecto>/consultar-proyecto/', views.consultar_proyecto, name='consultar_proyecto'),
	path('<int:id_proyecto>/modificar-proyecto/', views.modificar_proyecto, name='modificar_proyecto'),
]