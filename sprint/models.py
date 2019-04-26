from django.db import models


ESTADOS_SPRINT = (
    ('Pendiente', 'Pendiente'), # cuando se crea
    ('Activo', 'Activo'), # cuando se inicia
    ('Terminado', 'Terminado'),  # cuando finaliza
)

class Sprint(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_inicio = models.DateField('Fecha de Inicio Sprint')
    fecha_fin = models.DateField('Fecha de Fin Sprint')
    duracion = models.DurationField()
    proyecto = models.ForeignKey('proyecto.Proyecto',on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=25, choices=ESTADOS_SPRINT, default='Pendiente')
    def __str__(self):
        return self.nombre

