from django.db import models
from proyecto.models import Flujo,Proyecto

# Create your models here.

class TipoUserStory(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    flujos = models.ManyToManyField(Flujo, blank=False)
