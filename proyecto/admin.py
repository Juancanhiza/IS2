from django.contrib import admin

# Register your models here.
from .models import Proyecto
from rol.models import Rol
from rol.models import Permiso

admin.site.register(Proyecto)