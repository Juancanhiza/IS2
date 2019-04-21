import datetime
from django.db import models

# Create your models here.

ESTADOS_PROYECTO = (
    ('Pendiente', 'Pendiente'), # cuando se crea
    ('Activo', 'Activo'), # cuando se inicia
    ('Cancelado','Cancelado'), # cuando se cancela
    ('Terminado', 'Terminado'), # cuando se aprueba uno finalizado
    ('Suspendido', 'Suspendido'), # cuando se inactiva el proyecto
)

class Proyecto(models.Model):
    id = models.AutoField
    nombre = models.CharField(max_length=20)
    fecha_inicio = models.DateField('Fecha de Inicio Proyecto')
    fecha_fin = models.DateField('Fecha de Fin Proyecto')
    estado = models.CharField(max_length=25, choices=ESTADOS_PROYECTO, default='PEN')
    descripcion= models.TextField()

    def __str__(self):
        return self.nombre