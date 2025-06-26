from rest_framework import viewsets

from rest_framework import filters

from apps.core.models.suscripcion_model import Suscripcion
from apps.core.serializers.suscripcion_serializer import SuscripcionSerializer


class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer