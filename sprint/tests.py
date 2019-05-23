from django.test import TestCase
from sprint.models import *
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
