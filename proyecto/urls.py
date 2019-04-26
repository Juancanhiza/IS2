from django.conf.urls import url
from django.urls import path
from . import views
from tipoUserStory.views import tipoUserStoryListView, CreateUserStoryTypeView, UpdateUserStoryTypeView

urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(),name='project_list'),
	url(r'^create/$', views.CreateProjectView.as_view(), name='create_project'),
    url(r'^opciones/$', views.OptionsListView.as_view(), name='options_project'),
    path(route='update_project/<int:pk_proyecto>/', view=views.UpdateProjectView.as_view(), name='update_project'),
    path(route='opciones/<int:pk_proyecto>/', view=views.UpdateOptionsView.as_view(), name='update_options'),
    path(route='opciones/<int:pk_proyecto>/flujos/create/', view=views.CreateFlujoView.as_view(), name='create_options_flujo'),
    path(route='opciones/<int:pk_proyecto>/flujos/<int:pk>/', view=views.UpdateFlujoView.as_view(), name='update_options_flujo'),
    path(route='opciones/<int:pk_proyecto>/flujos/', view=views.FlujoListView.as_view(), name='update_options_flujo_list'),
    path(route='opciones/<int:pk_proyecto>/tipoUserStory/', view=tipoUserStoryListView.as_view(), name='user_story_type_list'),
    path(route='opciones/<int:pk_proyecto>/tipoUserStory/create/', view=CreateUserStoryTypeView.as_view(), name='create_user_story_type'),
	path(route='opciones/<int:pk_proyecto>/tipoUserStory/<int:pk>/', view=UpdateUserStoryTypeView.as_view(), name='update_user_story_type'),
    path(route='opciones/<int:pk_proyecto>/asignarRoles/', view=views.UpdateDetalleProyectoView.as_view(), name='update_roles_proyecto'),
]