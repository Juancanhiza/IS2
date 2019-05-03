from django.db import models

ESTADOS_SPRINT = (
    ('Pendiente', 'Pendiente'), # cuando se crea
    ('En Proceso', 'En Proceso'), # cuando se inicia
    ('Terminado', 'Terminado'),  # cuando finaliza
)


class Sprint(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    duracion = models.DurationField(blank=True, null=True)
    proyecto = models.ForeignKey('proyecto.Proyecto',on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=25, choices=ESTADOS_SPRINT, default='Pendiente')
    fecha_ini_estimada = models.DateField('Fecha de Inicio Estimada', blank=False, null=False)
    fecha_fin_estimada = models.DateField('Fecha de Fin Estimada', blank=False, null=False)

    def __str__(self):
        return self.nombre

