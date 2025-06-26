from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.core.views.articulo_view import ArticuloViewSet
from apps.core.views.suscripcion_view import SuscripcionViewSet
from apps.core.views.usuario_view import UsuarioViewSet
from apps.core.views.usuario_redactor_view import UsuarioRedactorViewSet

router = DefaultRouter()
router.register(r'articulos', ArticuloViewSet)
router.register(r'suscripciones', SuscripcionViewSet)
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'redactores', UsuarioRedactorViewSet, basename='redactor')


urlpatterns = [
    path('', include(router.urls)),
]
