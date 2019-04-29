from django.db import models
from proyecto.models import Proyecto
from flujo.models import Flujo


class TipoUserStory(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.TextField(null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, blank=False, null=False)
    flujos = models.ManyToManyField(Flujo, blank=False)
