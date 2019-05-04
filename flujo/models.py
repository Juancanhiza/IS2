from django.db import models


class Flujo(models.Model):
    proyecto = models.ForeignKey('proyecto.Proyecto', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)


class Fase(models.Model):
    flujo = models.ForeignKey(Flujo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
