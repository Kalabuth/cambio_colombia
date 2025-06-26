from django.contrib import admin

from apps.core.models.articulo_model import Articulo
from apps.core.models.suscripcion_model import Suscripcion
from apps.core.models.usuario_redactor_model import UsuarioRedactor

admin.site.register(UsuarioRedactor)
admin.site.register(Articulo)
admin.site.register(Suscripcion)
