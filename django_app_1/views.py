from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Usuario, Categoria, Producto, Inventario, CarritoCompra,
    CarritoDetalle, Venta, Recomendacion, ComandoVoz, Notificacion, Pago,
    Persona, Auto, Perro, PersonaPerro
)
from .serializers import (
    UsuarioSerializer, CategoriaSerializer, ProductoSerializer, InventarioSerializer,
    CarritoCompraSerializer, CarritoDetalleSerializer, VentaSerializer,
    RecomendacionSerializer, ComandoVozSerializer, NotificacionSerializer, PagoSerializer,
    PersonaSerializer, AutoSerializer, PerroSerializer, PersonaPerroSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class CarritoCompraViewSet(viewsets.ModelViewSet):
    queryset = CarritoCompra.objects.all()
    serializer_class = CarritoCompraSerializer

class CarritoDetalleViewSet(viewsets.ModelViewSet):
    queryset = CarritoDetalle.objects.all()
    serializer_class = CarritoDetalleSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class RecomendacionViewSet(viewsets.ModelViewSet):
    queryset = Recomendacion.objects.all()
    serializer_class = RecomendacionSerializer

class ComandoVozViewSet(viewsets.ModelViewSet):
    queryset = ComandoVoz.objects.all()
    serializer_class = ComandoVozSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class PerroViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    serializer_class = PerroSerializer

class PersonaPerroViewSet(viewsets.ModelViewSet):
    queryset = PersonaPerro.objects.all()
    serializer_class = PersonaPerroSerializer
