from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente =  models.CharField(max_length=100)
    descripcion_cliente = models.TextField(max_length=300)
    direccion_cliente = models.CharField(max_length=200)
    ruc_cliente = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_cliente
