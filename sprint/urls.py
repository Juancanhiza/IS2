from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', views.SprintListView.as_view(),name='sprint_list'),
	url(r'^create/$', views.CreateSprintView.as_view(), name='create_sprint'),
	path(route='update_sprint/<int:pk>/', view=views.UpdateSprintView.as_view(), name='update_sprint'),
]