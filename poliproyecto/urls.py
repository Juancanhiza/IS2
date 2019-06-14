"""poliproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from accounts.views import login, logout
from userstory.views import ver_archivo
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^proyectos/', include('proyecto.urls')),
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^roles/', include('rol.urls')),
    url(r'^clientes/',include('clientes.urls')),
    path(route='media/<int:archivo_id>/', view=ver_archivo, name='ver_archivo')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)