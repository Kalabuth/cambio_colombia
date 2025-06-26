from rest_framework import viewsets

from rest_framework import filters

from apps.core.models.articulo_model import Articulo
from apps.core.serializers.suscripcion_serializer import ArticuloSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['estado']

    def get_queryset(self):
        queryset = super().get_queryset()
        estado = self.request.query_params.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset