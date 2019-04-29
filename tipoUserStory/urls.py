from django.conf.urls import url
from django.urls import path
from .views import *

"""
URL para el tipo de User Story, crear, listar y modificar
"""
urlpatterns = [
    url(r'^$', tipoUserStoryListView.as_view(), name='user_story_type_list'),
    path('create/', view=CreateUserStoryTypeView.as_view(), name='create_user_story_type'),
    path('<int:pk>/', view=UpdateUserStoryTypeView.as_view(), name='update_user_story_type'),
]