from rest_framework import serializers

from apps.core.models.articulo_model import Articulo
from apps.core.models.suscripcion_model import Suscripcion

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = '__all__'

    def validate(self, data):
        usuario = data['usuario']
        fecha_inicio = data['fecha_inicio']
        fecha_fin = data['fecha_fin']

        if Suscripcion.objects.filter(
            usuario=usuario,
            fecha_inicio__lte=fecha_fin,
            fecha_fin__gte=fecha_inicio
        ).exists():
            raise serializers.ValidationError("El usuario ya tiene una suscripción activa.")
        return data
