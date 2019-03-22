from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

"""
URL para el login, y para cuando se loguea
"""

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
]
