from django.db import models
"""
Definimos los estados de un Sprint
"""
ESTADOS_SPRINT = (
    """
    Cuando se crea
    """
    ('Pendiente', 'Pendiente'),
    """
    Cuando se inicia
    """
    ('En Proceso', 'En Proceso'),
    """
    Cuando finaliza
    """
    ('Terminado', 'Terminado'),
)


"""
Se define el modelo Sprint
"""
class Sprint(models.Model):
    """
    Se definen los campos necesarios para el modelo
    """
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

