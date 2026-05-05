from django.test import TestCase
from rest_framework.test import APIClient

from .models import Equipo, Jugador


# Create your tests here.
class EquiposEndpoint(TestCase):
    def setUp(self):
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        equipo: Equipo =  Equipo.objects.create(
            nombre="Betis",
            pais="España",
            fecha_creacion="1980-04-20"
        )

        Jugador.objects.create(
            nickname="Juanito",
            rol="defensa",
            equipo=equipo
        )

    def test_equipos_list_endpoint(self):
        """Test list/GET of equipos"""
        response_from_api = self.client.get("/api/v1/")
        equipo_json = response_from_api.json()

        self.assertEqual(response_from_api.status_code, 200)

        self.assertEqual(len(equipo_json), 1)

        equipo = equipo_json[0]
        self.assertEqual(equipo["nombre"], "Betis")
        self.assertEqual(equipo["pais"], "España")
        self.assertEqual(equipo["fecha_creacion"], "1980-04-20")

        self.assertEqual(len(equipo["jugadores"]), 1)

        jugador = equipo["jugadores"][0]
        self.assertEqual(jugador['id'], 1 )
        self.assertEqual(jugador['nickname'], "Juanito")
        self.assertEqual(jugador['rol'], "defensa")

    def test_equipos_creation_endpoint(self):
        """Test creation/POST of equipos"""

        def get_equipos():
            response_from_api = self.client.get("/api/v1/")
            return response_from_api.json(), response_from_api

        # Before to creation, only placeholder equipo should exist.
        equipos, response = get_equipos()
        self.assertEqual(len(equipos), 1)

        # Creation of a new equipo
        response_from_api = self.client.post("/api/v1/",
                {"nombre": "Córdoba",
                      "pais": "España",
                      "fecha_creacion": "2013-09-04"
                 },format="json")
        self.assertEqual(response_from_api.status_code, 201)

        # After creation, two equipos should exist.
        equipos, response = get_equipos()
        equipo = equipos[1]
        self.assertEqual(len(equipos), 2)
        self.assertEqual(equipo['nombre'], "Córdoba")
        self.assertEqual(equipo['pais'], "España")
        self.assertEqual(equipo['fecha_creacion'], "2013-09-04")

    def test_equipos_retrieve_endpoint(self):
        """Test retrieve/GET of equipos"""
        response_from_api = self.client.get("/api/v1/1/")
        equipo = response_from_api.json()

        self.assertEqual(response_from_api.status_code, 200)

        self.assertEqual(equipo["nombre"], "Betis")
        self.assertEqual(equipo["pais"], "España")
        self.assertEqual(equipo["fecha_creacion"], "1980-04-20")

        self.assertEqual(len(equipo["jugadores"]), 1)

        jugador = equipo["jugadores"][0]
        self.assertEqual(jugador['id'], 1 )
        self.assertEqual(jugador['nickname'], "Juanito")
        self.assertEqual(jugador['rol'], "defensa")