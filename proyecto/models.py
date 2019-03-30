import datetime
from django.db import models

# Create your models here.

class Proyecto(models.Model):
    id_proyecto = models.AutoField
    nombre_proyecto = models.CharField(max_length=20)
    fecha_inicio_proyecto = models.DateField('Fecha de Inicio Proyecto')
    fecha_fin_proyecto = models.DateField('Fecha de Fin Proyecto')
    activo = 'Activo'
    cancelado = 'Cancelado'
    suspendido = 'Suspendido'
    finalizado = 'Finalizado'
    estado_opciones = ((activo, 'Activo'), (cancelado,'Cancelado'), (suspendido, 'Suspendido'), (finalizado, 'Finalizado'))
    estado_proyecto = models.CharField(max_length=25, choices= estado_opciones, default=activo)
    descripcion_proyecto = models.TextField()

    def __str__(self):
        return self.nombre_proyecto

