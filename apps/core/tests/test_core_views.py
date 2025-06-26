import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APIClient

from apps.core.models.usuario_redactor_model import UsuarioRedactor
from apps.core.models.articulo_model import Articulo
from apps.core.models.suscripcion_model import Suscripcion


@pytest.mark.django_db
class TestVistasAPI:

    def setup_method(self):
        self.client = APIClient()
        self.usuario = User.objects.create_user(username='usuario_prueba', password='123456')
        self.redactor = UsuarioRedactor.objects.create(
            nombre_completo='Laura Redactora',
            correo='laura@correo.com',
            activo=True
        )

    def test_crear_articulo_exitosamente(self):
        respuesta = self.client.post('/api/articulos/', {
            "titulo": "Artículo de prueba",
            "contenido": "Contenido del artículo",
            "fecha_publicacion": timezone.now().date(),
            "estado": "borrador",
            "autor": self.redactor.id
        }, format='json')

        assert respuesta.status_code == 201
        assert respuesta.data['titulo'] == "Artículo de prueba"

    def test_obtener_detalle_articulo(self):
        articulo = Articulo.objects.create(
            titulo="Detalle",
            contenido="Contenido del detalle",
            fecha_publicacion=timezone.now().date(),
            estado="publicado",
            autor=self.redactor
        )

        respuesta = self.client.get(f'/api/articulos/{articulo.id}/')
        assert respuesta.status_code == 200
        assert respuesta.data['titulo'] == "Detalle"

    def test_filtrar_articulos_por_estado(self):
        Articulo.objects.create(
            titulo="Publicado",
            contenido="Texto",
            fecha_publicacion=timezone.now().date(),
            estado="publicado",
            autor=self.redactor
        )
        Articulo.objects.create(
            titulo="Borrador",
            contenido="Texto",
            fecha_publicacion=timezone.now().date(),
            estado="borrador",
            autor=self.redactor
        )

        respuesta = self.client.get('/api/articulos/?estado=publicado')
        assert respuesta.status_code == 200
        for articulo in respuesta.data:
            assert articulo['estado'] == 'publicado'

    def test_crear_suscripcion_valida(self):
        fecha_inicio = timezone.now().date()
        fecha_fin = fecha_inicio + timedelta(days=30)

        respuesta = self.client.post('/api/suscripciones/', {
            "usuario": self.usuario.id,
            "tipo": "pago",
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin
        }, format='json')

        assert respuesta.status_code == 201
        assert respuesta.data['tipo'] == "pago"

    def test_suscripcion_conflicto_activa(self):
        fecha_inicio = timezone.now().date()
        fecha_fin = fecha_inicio + timedelta(days=30)

        Suscripcion.objects.create(
            usuario=self.usuario,
            tipo="pago",
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )

        respuesta = self.client.post('/api/suscripciones/', {
            "usuario": self.usuario.id,
            "tipo": "gratuita",
            "fecha_inicio": fecha_inicio + timedelta(days=5),
            "fecha_fin": fecha_fin + timedelta(days=5)
        }, format='json')

        assert respuesta.status_code == 400
        assert "activa" in str(respuesta.data).lower()
