from django.core.exceptions import ValidationError
from django.db import models

PENDIENTE = 2
ASIGNADO = 1
FINALIZADO = 0
ESTADOS_US = (
    (PENDIENTE, 'Pendiente'), # cuando se crea
    (ASIGNADO, 'Asignado'), # cuando se asigna a un sprint
    (FINALIZADO,'Finalizado'), # cuando se finaliza
)


def rango(valor):
    """Validación de rango permitido"""
    if valor >10 or valor < 0:
        raise ValidationError('El valor debe estar en 0-10')

class UserStory(models.Model):
    '''Modelo de User Story'''
    '''Campos:'''
    proyecto = models.ForeignKey('proyecto.Proyecto',on_delete=models.CASCADE,null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    fecha_inicio = models.DateField('Fecha de inicio del User Story')
    duracion_estimada = models.DurationField()
    valor_negocio = models.PositiveIntegerField(validators=[rango])
    prioridad = models.PositiveIntegerField(validators=[rango])
    valor_tecnico = models.PositiveIntegerField(validators=[rango])
    estado = models.PositiveIntegerField( default=PENDIENTE, choices=ESTADOS_US)
    team_member =  models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, null=True)
    sprint = models.ForeignKey('sprint.Sprint', on_delete=models.PROTECT, null=True, blank=True)
    '''tipo user story'''

    def __str__(self):
        return self.nombre

    def set_priorizacion(self):
        return (2*self.valor_negocio + self.prioridad + 2*self.valor_tecnico)/4

    priorizacion = property(set_priorizacion)
