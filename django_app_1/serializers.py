from rest_framework import serializers
from .models import (
    Usuario, Categoria, Producto, Inventario, CarritoCompra,
    CarritoDetalle, Venta, Recomendacion, ComandoVoz, Notificacion,
    Pago, Persona, Auto, Perro, PersonaPerro
)

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ¡Campo solo para escritura!

    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Usamos el método create_user del manager para hashear la contraseña
        return Usuario.objects.create_user(
            correo=validated_data['correo'],
            nombre=validated_data['nombre'],
            password=validated_data['password'],
            rol=validated_data.get('rol', 'cliente')
        )

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class CarritoCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompra
        fields = '__all__'

class CarritoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoDetalle
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacion
        fields = '__all__'

class ComandoVozSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComandoVoz
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombre', 'edad']

class AutoSerializer(serializers.ModelSerializer):
    persona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())

    class Meta:
        model = Auto
        fields = ['id', 'marca', 'modelo', 'persona']


class PerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perro
        fields = ['id', 'nombre', 'raza']

class PersonaPerroSerializer(serializers.ModelSerializer):
    persona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())
    perro = serializers.PrimaryKeyRelatedField(queryset=Perro.objects.all())

    class Meta:
        model = PersonaPerro
        fields = ['id', 'persona', 'perro']
