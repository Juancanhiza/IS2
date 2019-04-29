from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

ESTADOS_USUARIO = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo')
)

class Usuario(AbstractUser):
    ''' Implementa la clase de Usuarios, hereda campos de AbstractUser en la que se
    encuentran campos necesarios como Nombre, Apellido, Contraseña, email, '''
    estado = models.CharField(max_length=8, choices=ESTADOS_USUARIO, default='Activo')
    ci = models.CharField(max_length=10, null=True, blank=True)
    telefono= models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    permisos = models.ManyToManyField('rol.Permiso', blank=False)
    email = models.EmailField('Email', blank=False, null=False)

    def __str__(self):
        return self.username


