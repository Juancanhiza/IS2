from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse


"""
Vista del Login
"""

def list(request):
    """
    Vista de la pagina de inicio
    :param request:
    """
    return render(request, '../templates/proyecto/list.html')