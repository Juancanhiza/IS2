import unittest
from userstory.models import UserStory
from proyecto.models import Proyecto

class Test(unittest.TestCase):
    """
    Test para creación de US
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