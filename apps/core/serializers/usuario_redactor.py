from rest_framework import serializers

from apps.core.models.usuario_redactor_model import UsuarioRedactor

class UsuarioRedactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRedactor
        fields = ['id', 'nombre_completo', 'correo', 'activo']
