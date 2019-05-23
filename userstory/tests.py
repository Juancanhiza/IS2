import unittest
from userstory.models import UserStory, Actividad, Archivo, Nota
from proyecto.models import Proyecto

class Test(unittest.TestCase):
    """
    Test para creacion de US
    """
    def test_creacionUs(self):
        us = UserStory()
        self.assertIsNotNone(us)
    """
    Test de Rango permitido
    """
    def test_Rango(self):
        proyecto1 = Proyecto(nombre='Proyecto1', fecha_inicio='23/04/2019', fecha_fin='22/04/2019')
        us = UserStory(proyecto=proyecto1, nombre="p1", descripcion="desc", fecha_inicio='13/04/2019', duracion_estimada=100, valor_negocio=55)
        self.assertLessEqual(us.valor_negocio, 10)

<<<<<<< HEAD
    """
    Test de validacion que verifica que un User Story tenga un team member asignado antes de 
    asignar a un sprint
    """
    def test_team_member_asignacion(self):
        us = UserStory()
        us.duracion_estimada = 30
        us.team_member = 2
        print('duracion estimada: ' + str(us.duracion_estimada))
        print('team member: ' + str(us.team_member))
        us.validate_asignacion()
        print('valido')
        us.team_member = None
        print('duracion estimada: ' + str(us.duracion_estimada))
        print('team member: ' + str(us.team_member))
        us.validate_asignacion()

    """
    Test de validacion que verifica que un User Story tenga una duracion estimada antes de 
    asignar a un sprint
    """
    def test_duracion_estimada_asignacion(self):
        us = UserStory()
        us.duracion_estimada = 30
        us.team_member = 2
        print('duracion estimada: ' + str(us.duracion_estimada))
        print('team member: ' + str(us.team_member))
        us.validate_asignacion()
        print('valido')
        us.duracion_estimada = 0
        print('duracion estimada: ' + str(us.duracion_estimada))
        print('team member: ' + str(us.team_member))
        us.validate_asignacion()
=======
    def test_actividad(self):
        actividad = Actividad(nombre='Actividad 1', descripcion='desc', duracion='1000')
        self.assertIsNotNone(actividad)

    def test_archivo(self):
        archivo = Archivo(titulo='Archivo 1')
        self.assertIsNotNone(archivo)

    def test_nota(self):
        nota = Nota(nota='Nota 1')
        self.assertIsNotNone(nota)
>>>>>>> c257919e0c2f064d19b2ecd0b840e1490b97099f
