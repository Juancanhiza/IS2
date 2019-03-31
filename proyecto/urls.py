from django.conf.urls import url
from django.urls import path
from . import views

"""
URL para el login, y para cuando se loguea
"""
urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(),name='project_list'),
	url(r'^create/$', views.CreateProjectView.as_view(), name='create_project'),
	path(route='update_project/<int:pk>/', view=views.UpdateProjectView.as_view(), name='update_project'),
]