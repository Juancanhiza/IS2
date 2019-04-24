from django.db import models
from typing import Any
from django.core.exceptions import ValidationError
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class UserStory(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    fecha_inicio = models.DateField('Fecha de inicio del User Story')
    duracion_estimada = models.DurationField()
    valor_negocio = models.PositiveIntegerField()
    prioridad = models.PositiveIntegerField()
    valor_tecnico = models.PositiveIntegerField()
    '''tipo user story'''
    '''team member'''
    def __str__(self):
        return self.nombre

    '''def valor_negocio_validacion(self):
        if self.valor_negocio >10:
             raise ValidationError('Valor entre 0 y 10')'''

    def set_priorizacion(self):
        return (2*self.valor_negocio + self.prioridad + 2*self.valor_tecnico)/4

    priorizacion = property(set_priorizacion)

    def validate_even(value):
        if value > 10:
            raise ValidationError(
                _('%(value) debe estar entre 0 y 10'),
                params={'value': value},
            )