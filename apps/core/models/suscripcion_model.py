from django.db import models
from django.contrib.auth.models import User

from apps.common.models.base_model import BaseModel


class Suscripcion(BaseModel):
    class TipoSuscripcion(models.TextChoices):
        GRATUITA = 'gratuita', 'Gratuita'
        PAGO = 'pago', 'Pago'

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TipoSuscripcion.choices)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo}"