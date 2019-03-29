from django.conf.urls import url
from django.urls import path
from . import views

app_name = "usuarios"
urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^add', views.add, name='add'),
    path('<int:id_usuario>/modify/', views.modify, name='modify'),
    path('<int:id_usuario>/query/', views.query, name='query'),
]