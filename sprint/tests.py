from django.test import TestCase
from sprint.models import *
import time
from flujo.views import TableroTemplateView
from proyecto.models import *

class SprintModelTest(TestCase):
    """
    Clase de Tests del modelo sprint
    """
    def test_creacion(self):
        """
        verifica que los sprints se guarden correctamente en un estado valido
        """
        proyecto = Proyecto(
                nombre="prueba",
                estado="Pendiente",
                descripcion="proyecto de prueba"
                )
        proyecto.save()
        sprint = Sprint(
            nombre="prueba",
            proyecto=proyecto.pk,
            estado='Pendiente',
            dias_laborales=20,
            dias_habiles='1,2,3,4,5'
            )
        sprint.validate()
        sprint.save()
        get_sprint = Sprint.objects.get(pk=sprint.pk)
        sprint.delete()
        proyecto.delete()

    def test_validacion_nombre(self):
        """
        Verifica que la validacion de obligatoriedad del campo nombre se ejecute correctamente
        """
        sprint = Sprint(
            proyecto=3,
            estado='Pendiente',
            dias_laborales=20,
            dias_habiles='1,2,3,4,5'
        )
        sprint.validate()

    def test_validacion_proyecto(self):
        """
        Verifica que la validacion de obligatoriedad del campo proyecto se ejecute correctamente
        """
        sprint = Sprint(
            nombre='prueba',
            estado='Pendiente',
            dias_laborales=20,
            dias_habiles='1,2,3,4,5'
        )
        sprint.validate()

    def test_validacion_dias_laborales(self):
        """
        Verifica que la validacion de obligatoriedad del campo dias laborales se ejecute correctamente
        """
        sprint = Sprint(
            nombre='prueba',
            proyecto=3,
            estado='Pendiente',
            dias_habiles='1,2,3,4,5'
        )
        sprint.validate()

    def test_validacion_dias_laborales(self):
        """
        Verifica que la validacion de obligatoriedad del campo dias habiles se ejecute correctamente
        """
        sprint = Sprint(
            nombre='prueba',
            proyecto=3,
            estado='Pendiente',
            dias_laborales=20
        )
        sprint.validate()

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
