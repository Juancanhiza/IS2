import unittest
from rol.models import *

class Test(unittest.TestCase):
    """
    Test de creacion de Rol vacio
    """
    def test_creacionRol(self):
        rol1 = Rol()
        self.assertIsNotNone(rol1)
