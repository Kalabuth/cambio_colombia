# apps/core/views.py

from rest_framework import viewsets

from apps.core.models.usuario_redactor_model import UsuarioRedactor
from apps.core.serializers.usuario_redactor import UsuarioRedactorSerializer


class UsuarioRedactorViewSet(viewsets.ModelViewSet):
    queryset = UsuarioRedactor.objects.all()
    serializer_class = UsuarioRedactorSerializer
