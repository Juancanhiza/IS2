from django.conf.urls import url
from django.urls import path
from .views import *

"""
URL para el Sprint crear, listar y modificar
"""
urlpatterns = [
    url(r'^$', SprintListView.as_view(), name='sprint_list'),
    path('create/', view=CreateSprintView.as_view(), name='create_sprint'),
    path('<int:pk>/', view=UpdateSprintView.as_view(), name='update_sprint'),
]