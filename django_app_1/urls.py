from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, CategoriaViewSet, ProductoViewSet, InventarioViewSet,
    CarritoCompraViewSet, CarritoDetalleViewSet, VentaViewSet, RecomendacionViewSet,
    ComandoVozViewSet, NotificacionViewSet, PagoViewSet, PersonaViewSet, AutoViewSet, 
    PerroViewSet, PersonaPerroViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'inventarios', InventarioViewSet)
router.register(r'carritos_compra', CarritoCompraViewSet)
router.register(r'carritos_detalle', CarritoDetalleViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'recomendaciones', RecomendacionViewSet)
router.register(r'comandos_voz', ComandoVozViewSet)
router.register(r'notificaciones', NotificacionViewSet)
router.register(r'pagos', PagoViewSet)
router.register(r'personas', PersonaViewSet)
router.register(r'autos', AutoViewSet)
router.register(r'perros', PerroViewSet)
router.register(r'personas_perros', PersonaPerroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
