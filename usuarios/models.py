from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    id_usuario = models.AutoField
    nombre_usuario = models.CharField(max_length=100)
    apellido_usuario = models.CharField(max_length=100)
    contraseña_usuario = models.CharField(max_length=100)
    activo = 'Activo'
    inactivo = 'Inactivo'
    estado_opciones = ((activo,'Activo'),(inactivo,'Inactivo'))
    estado_usuario = models.CharField(max_length=8,choices=estado_opciones,default=activo)
    ci_usuario = models.CharField(max_length=10)
    telefono_usuario = models.CharField(max_length=50)
    direccion_usuario = models.CharField(max_length=200)
    descripcion_usuario = models.TextField()

    def __str__(self):
        return self.nombre_usuario


