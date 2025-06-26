import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestUsuarioAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_crear_usuario_exitosamente(self):
        datos = {
            "username": "usuario_test",
            "email": "usuario@test.com",
            "password": "clave_segura123"
        }

        respuesta = self.client.post('/api/usuarios/', datos, format='json')

        assert respuesta.status_code == 201
        assert respuesta.data['username'] == datos['username']
        assert 'id' in respuesta.data
        assert User.objects.filter(username="usuario_test").exists()

    def test_creacion_falla_por_password_corto(self):
        datos = {
            "username": "usuario_corto",
            "email": "corto@test.com",
            "password": "123"
        }

        respuesta = self.client.post('/api/usuarios/', datos, format='json')

        assert respuesta.status_code == 400
        assert 'password' in respuesta.data

    def test_creacion_falla_si_username_ya_existe(self):
        User.objects.create_user(username="repetido", email="old@test.com", password="algo123")

        datos = {
            "username": "repetido",
            "email": "nuevo@test.com",
            "password": "clave1234"
        }

        respuesta = self.client.post('/api/usuarios/', datos, format='json')

        assert respuesta.status_code == 400
        assert 'username' in respuesta.data
