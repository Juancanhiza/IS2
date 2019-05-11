import unittest
import time
from sprint.models import Sprint
from flujo.views import TableroTemplateView

class Test(unittest.TestCase):
    """
    Tests de Sprint
    """
    def test_creacionSprint(self):
        sprint = Sprint()
        self.assertIsNotNone(sprint)
    
    def test_fechasSprint(self):
        sprint = Sprint(nombre='sprint', fecha_inicio='29/04/2019', fecha_fin='12/04/2019')
        fechaInicio = time.strptime(sprint.fecha_inicio, "%d/%m/%Y")
        fechaFin = time.strptime(sprint.fecha_fin, "%d/%m/%Y")
        self.assertLessEqual(fechaInicio, fechaFin, "La Fecha de Inicio de Sprint debe ser menor a la fecha de Fin")

    def test_tablero(self):
        tablero = TableroTemplateView()
        self.assertIsNotNone(tablero)

    def test_duracion(self):
        sprint = Sprint(nombre='sprint', fecha_inicio='29/04/2019', fecha_fin='12/04/2019', duracion=200)
        self.assertIs(sprint.duracion, 200)