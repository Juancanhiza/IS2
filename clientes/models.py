from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    direccion = models.CharField(max_length=200)
    ruc = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_cliente
