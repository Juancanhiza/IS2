import pickle

from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponse

"""
Definicion de los estados de User Story
"""
PENDIENTE = 2
ASIGNADO = 1
FINALIZADO = 0
ESTADOS_US = (
    (PENDIENTE, 'Pendiente'),
    (ASIGNADO, 'Asignado'),
    (FINALIZADO,'Finalizado')
)

"""
Se definen los estados en fase
"""

ESTADOS_EN_FASE = (
    ('To Do', 'To Do'),
    ('Doing', 'Doing'),
    ('Done', 'Done'),
    ('Control de Calidad', 'Control de Calidad'),
)

"""
Metodo que realiza la validacion del rango permitido para los campos de: Valor de Negocio, Prioridad y Valor tecnico 
"""
def rango(valor):
    """
    Validación de rango permitido
    """
    if valor >10 or valor < 0:
        raise ValidationError('El valor debe estar en 0-10')

"""
Se define el modelo User Story
"""
class UserStory(models.Model):
    """
    Modelo de la clase User Story, el cual representa un conjunto de tareas a ser realizadas
    en un periodo de tiempo especificado
    """
    sprints_asignados = models.ManyToManyField('sprint.Sprint', blank=True, related_name='userstory_sprint_asignado')
    estado_fase = models.CharField(max_length=30, choices=ESTADOS_EN_FASE, default='To Do')
    flujo = models.ForeignKey('flujo.Flujo', on_delete=models.PROTECT)
    fase = models.ForeignKey('flujo.Fase', on_delete=models.PROTECT, null=True, blank=True)
    proyecto = models.ForeignKey('proyecto.Proyecto', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    fecha_inicio = models.DateField('Fecha de inicio del User Story', null=True, blank=True)
    duracion_estimada = models.PositiveIntegerField(null=True)
    duracion_restante = models.IntegerField(null=True,blank=True)
    valor_negocio = models.PositiveIntegerField(validators=[rango])
    prioridad = models.PositiveIntegerField(validators=[rango])
    valor_tecnico = models.PositiveIntegerField(validators=[rango])
    estado = models.PositiveIntegerField(default=PENDIENTE, choices=ESTADOS_US)
    team_member = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, blank=True, null=True)
    tipo_us = models.ForeignKey('tipoUserStory.TipoUserStory', on_delete=models.PROTECT)
    sprint = models.ForeignKey('sprint.Sprint', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        """
        Retorna el nombre del User Story actual
        :return: nombre del objeto actual
        """
        return self.nombre

    def set_priorizacion(self):
        return (2*self.valor_negocio + self.prioridad + 2*self.valor_tecnico)/4

    priorizacion = property(set_priorizacion)

    def has_team_member(self):
        """
        retorna falso si el user story no esta asignado a ningun team member, en caso contrario
        retorna verdadero
        :return: True o False
        """
        if not self.team_member:
            return False
        return True

    def has_duracion_estimada(self):
        """
        retorna falso si el user story no tiene una duracion estimada o su duracion
         estimada es 0, en caso contrario retorna verdadero
        :return: True o False
        """
        if not self.duracion_estimada or self.duracion_estimada == 0:
            return False
        return True

    def validate_asignacion(self):
        """
        retorna falso si el user story no tiene un team member asignado o si no se le ha
        asignado una duracion estimada o su duracion estimada es 0
        :return: True o Excepcion
        """
        if not self.has_team_member():
            raise ValidationError('Debe asignar un team member al user story ' + str(self.nombre))
        if not self.has_duracion_estimada():
            raise ValidationError('Se deben estimar las horas de duración del user story ' + str(self.nombre))
        if not self.duracion_restante:
            raise ValidationError('Se deben estimar las horas de duración del user story ' + str(self.nombre))
        if self.duracion_restante <= 0:
            raise ValidationError('Debe indicar una duracion estimada mayor a 0 al user story ' + str(self.nombre))
        return True

    def get_horas_trabajadas(self, sprint=None):
        """
        metodo de la clase de user stories que retorna la cantidad de horas trabajadas
        hasta el momento en el user story
        :return: las horas trabajadas en el user story actual
        """
        if not sprint:
            actividades = Actividad.objects.filter(us=self.pk)
        else:
            actividades = Actividad.objects.filter(us=self.pk, sprint=sprint)
        horas = 0.0
        for actividad in actividades:
            horas += actividad.duracion
        return horas


class Nota(models.Model):
    """
        Clase para adjuntar una nota a un US
    """
    nota = models.TextField()
    us = models.ForeignKey('UserStory', on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    sprint = models.ForeignKey('sprint.Sprint', on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna el contenido de la nota actual
        :return: campo nota del objeto actual
        """
        return self.nota


class Archivo(models.Model):
    """
    Clase para adjuntar un archivo a un US
    """
    titulo = models.CharField(max_length=255, blank=True)
    archivo = models.FileField(upload_to='')
    binario = models.BinaryField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    us = models.ForeignKey('UserStory', on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT, null=True)
    sprint = models.ForeignKey('sprint.Sprint', on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna el titulo del Archivo actual
        :return: titulo del objeto actual
        """
        return self.titulo

    def set_data(self, data):
        self.binario = pickle.dumps(data)

    def get_data(self):
        return pickle.loads(self.binario)

class Actividad(models.Model):
    """
    Clase para agregar una actividad a un User Story
    """
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)
    us = models.ForeignKey('UserStory', on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField()
    sprint = models.ForeignKey('sprint.Sprint', on_delete=models.CASCADE)
    fase_us = models.ForeignKey('flujo.Fase', on_delete=models.CASCADE,null=True,blank=True)
    estado_fase = models.CharField(max_length=30, choices=ESTADOS_EN_FASE, default='To Do')

    def __str__(self):
        """
        Retorna el nombre del objeto actual
        :return: nombre del objeto actual
        """
        return self.nombre

class CambioEstado(models.Model):
    descripcion = models.TextField()
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)
    us = models.ForeignKey('UserStory', on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    sprint = models.ForeignKey('sprint.Sprint', on_delete=models.CASCADE)
    fase = models.ForeignKey('flujo.Fase', on_delete=models.CASCADE,null=True)
    estado_fase = models.CharField(max_length=30, choices=ESTADOS_EN_FASE, null=True, blank=True)

    def __str__(self):
        """
        Retorna la descripcion del objeto actual
        :return: descripcion del objeto actual
        """
        return self.descripcion

class HistorialEstimaciones(models.Model):
    duracion_estimada = models.PositiveIntegerField()
    sprint = models.ForeignKey('sprint.Sprint', on_delete=models.CASCADE)
    us = models.ForeignKey('UserStory', on_delete=models.CASCADE, null=True)