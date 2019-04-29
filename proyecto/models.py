import datetime
from django.db import models
from rol.models import Rol
from usuarios.models import Usuario

# Create your models here.

ESTADOS_PROYECTO = (
    ('Pendiente', 'Pendiente'), # cuando se crea
    ('Activo', 'Activo'), # cuando se inicia
    ('Cancelado','Cancelado'), # cuando se cancela
    ('Terminado', 'Terminado'), # cuando se aprueba uno finalizado
    ('Suspendido', 'Suspendido'), # cuando se inactiva el proyecto
)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=25, choices=ESTADOS_PROYECTO, default='Pendiente')
    descripcion= models.TextField(blank=True, null=True)
    fecha_ini_estimada = models.DateField('Fecha de Inicio Estimada', blank=False, null=False)
    fecha_fin_estimada = models.DateField('Fecha de Fin Estimada', blank=False, null=False)

    def __str__(self):
        return self.nombre


class TeamMember(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank=False, null=False)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, blank=False, null=False)
