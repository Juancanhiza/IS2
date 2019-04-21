from django.conf.urls import url
from django.urls import path
from . import views

"""
URL para el tipo de User Story, crear, listar y modificar
"""
urlpatterns = [
    url(r'^$', views.tipoUserStoryListView.as_view(), name='user_story_type_list'),
	url(r'^create/$', views.CreateUserStoryTypeView.as_view(), name='create_user_story_type'),
	path(route='update_user_story_type/<int:pk>/', view=views.UpdateUserStoryTypeView.as_view(), name='update_user_story_type'),
]