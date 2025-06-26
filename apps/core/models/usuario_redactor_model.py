from django.db import models

from apps.common.models.base_model import BaseModel

class UsuarioRedactor(BaseModel):
    nombre_completo = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_completo