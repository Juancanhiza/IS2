from django.conf.urls import url
from django.urls import path
from . import views

"""
URL para Usuarios: crear, listar, modificar
"""
urlpatterns = [
    url(r'^$', views.UserListView.as_view(),name='user_list'),
	url(r'^create/$', views.CreateUserView.as_view(), name='create_user'),
	path(route='modificar/<int:pk>/', view=views.UpdateUserView.as_view(), name='update_user'),
	path(route='ver/<int:pk>/', view=views.VerUserDetailView.as_view(), name='ver_user')
]