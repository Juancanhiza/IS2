from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(max_length=300, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=False, null=True)
    ruc = models.CharField(max_length=50, blank=False, null=True, unique=True)
    telefono = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.nombre
