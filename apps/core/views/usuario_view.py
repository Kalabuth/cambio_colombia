from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.core.serializers.usuario_serializer import UsuarioSerializer


class UsuarioViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UsuarioSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
