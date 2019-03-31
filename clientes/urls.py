from django.urls import path
from django.conf.urls import url
from . import views
# from django.contrib.auth.views import login

"""
Definicion de URLs contenidas en clientes
"""

urlpatterns = [
    url(r'^$', views.ClientListView.as_view(),name='client_list'),
	url(r'^create/$', views.CreateClientView.as_view(), name='create_client'),
	path(route='update_client/<int:pk>/', view=views.UpdateClientView.as_view(), name='update_client'),
]