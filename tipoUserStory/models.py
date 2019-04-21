from django.db import models

# Create your models here.

class TipoUserStory(models.Model):
    id = models.AutoField
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    # Falta el Flujo!
