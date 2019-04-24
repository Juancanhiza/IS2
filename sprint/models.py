from django.db import models


class Sprint(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_inicio = models.DateField('Fecha de Inicio Sprint')
    fecha_fin = models.DateField('Fecha de Fin Sprint')
    duracion = models.DurationField()

    def __str__(self):
        return self.nombre

