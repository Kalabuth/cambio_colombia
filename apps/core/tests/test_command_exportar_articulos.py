import pytest
import os
import csv
from django.core.management import call_command
from django.utils import timezone

from apps.core.models.articulo_model import Articulo
from apps.core.models.usuario_redactor_model import UsuarioRedactor


@pytest.mark.django_db
class TestExportarArticulosCommand:

    def setup_method(self):
        self.redactor = UsuarioRedactor.objects.create(
            nombre_completo="Test Redactor",
            correo="redactor@test.com",
            activo=True
        )

        self.articulo_1 = Articulo.objects.create(
            titulo="Publicado 1",
            contenido="...",
            fecha_publicacion=timezone.now().date(),
            estado="publicado",
            autor=self.redactor
        )

        self.articulo_2 = Articulo.objects.create(
            titulo="Borrador",
            contenido="...",
            fecha_publicacion=timezone.now().date(),
            estado="borrador",
            autor=self.redactor
        )

    def teardown_method(self):
        if os.path.exists('articulos_exportados.csv'):
            os.remove('articulos_exportados.csv')

    def test_exporta_solo_publicados(self):
        call_command('exportar_articulos')

        assert os.path.exists('articulos_exportados.csv')

        with open('articulos_exportados.csv', newline='', encoding='utf-8') as f:
            lector = list(csv.reader(f))
            assert len(lector) == 2 
            assert lector[1][1] == self.articulo_1.titulo
