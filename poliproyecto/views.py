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
from django.contrib.auth.decorators import login_required


"""
Vista del Login
"""

def home(request):
    """
    Vista de la pagina de inicio
    :param request:
    """
    return render(request, '../templates/accounts/home.html')

@login_required
def index(request):
    """
    Vista de la pagina de saludo, luego del inicio de sesion
    :param request:
    """
    context = {
        'username': request.user,
    }
    return render(request, '../templates/accounts/index.html',context)