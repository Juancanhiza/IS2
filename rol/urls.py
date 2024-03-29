from django.conf.urls import url
from django.urls import path
from . import views
"""
URL para el ver, crear y modificar roles
"""

urlpatterns = [
	url(r'^$', views.RolListView.as_view(),name='rol_list'),
	url(r'^create/$', views.CreateRolView.as_view(), name='create_rol'),
	path(route='modificar/<int:pk>/', view=views.UpdateRolView.as_view(), name='update_rol'),
	path(route='ver/<int:pk>/', view=views.VerRolDetailView.as_view(), name='ver_rol')
]