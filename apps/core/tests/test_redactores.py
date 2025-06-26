import pytest
from rest_framework.test import APIClient

from apps.core.models.usuario_redactor_model import UsuarioRedactor


@pytest.mark.django_db
class TestUsuarioRedactorAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_crear_redactor_exitosamente(self):
        datos = {
            "nombre_completo": "Carolina Martínez",
            "correo": "carolina@medio.com",
            "activo": True
        }

        respuesta = self.client.post('/api/redactores/', datos, format='json')

        assert respuesta.status_code == 201
        assert respuesta.data["nombre_completo"] == datos["nombre_completo"]
        assert "id" in respuesta.data
        assert UsuarioRedactor.objects.filter(correo="carolina@medio.com").exists()

    def test_creacion_falla_por_falta_de_campos(self):
        datos = {
            "correo": "sin_nombre@medio.com"
        }

        respuesta = self.client.post('/api/redactores/', datos, format='json')

        assert respuesta.status_code == 400
        assert "nombre_completo" in respuesta.data

    def test_listar_redactores(self):
        UsuarioRedactor.objects.create(
            nombre_completo="Laura Torres", correo="laura@medio.com", activo=True
        )
        UsuarioRedactor.objects.create(
            nombre_completo="Carlos Pérez", correo="carlos@medio.com", activo=False
        )

        respuesta = self.client.get('/api/redactores/')

        assert respuesta.status_code == 200
        assert len(respuesta.data) == 2
        nombres = [r["nombre_completo"] for r in respuesta.data]
        assert "Laura Torres" in nombres
        assert "Carlos Pérez" in nombres
