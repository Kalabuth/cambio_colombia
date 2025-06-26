from django.db import models
from django.utils import timezone

from apps.core.models.usuario_redactor_model import UsuarioRedactor
from apps.common.models.base_model import BaseModel


class Articulo(BaseModel):
    class EstadoArticulo(models.TextChoices):
        BORRADOR = 'borrador', 'Borrador'
        PUBLICADO = 'publicado', 'Publicado'

    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=10, choices=EstadoArticulo.choices, default=EstadoArticulo.BORRADOR)
    autor = models.ForeignKey(UsuarioRedactor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo