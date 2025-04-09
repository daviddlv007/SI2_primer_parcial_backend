from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo es obligatorio')
        if not nombre:
            raise ValueError('El nombre es obligatorio')
        
        correo = self.normalize_email(correo)
        usuario = self.model(
            correo=correo,
            nombre=nombre,
            **extra_fields
        )
        usuario.set_password(password)  # Hashea la contraseña de forma segura
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, nombre, password, **extra_fields):
        extra_fields.setdefault('rol', 'admin')
        return self.create_user(correo, nombre, password, **extra_fields)


class Usuario(AbstractBaseUser):
    last_login = None

    class Role(models.TextChoices):
        ADMIN = 'admin', 'Administrador'
        CLIENTE = 'cliente', 'Cliente'

    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    rol = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CLIENTE
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    umbral_alerta = models.IntegerField(default=5)

    def __str__(self):
        return f"Inventario de {self.producto.nombre}"

class CarritoCompra(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('finalizado', 'Finalizado'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return f"Carrito de {self.usuario.nombre} ({self.estado})"

class CarritoDetalle(models.Model):
    carrito = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle: {self.producto.nombre} en carrito {self.carrito.id}"

class Venta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    carrito = models.ForeignKey(CarritoCompra, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Venta {self.id} - Usuario: {self.usuario.nombre}"

class Recomendacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"Recomendación para {self.usuario.nombre} de {self.producto.nombre}"

class ComandoVoz(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comando_texto = models.CharField(max_length=255)

    def __str__(self):
        return f"Comando de {self.usuario.nombre}"

class Notificacion(models.Model):
    TIPO_CHOICES = [
        ('stock_bajo', 'Stock Bajo'),
        ('promocion', 'Promoción'),
        ('alerta', 'Alerta'),
        ('otro', 'Otro'),
    ]
    ESTADO_CHOICES = [
        ('enviado', 'Enviado'),
        ('pendiente', 'Pendiente'),
        ('fallido', 'Fallido'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    mensaje = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Notificación: {self.mensaje}"

class Pago(models.Model):
    ESTADO_PAGO_CHOICES = [
        ('exitoso', 'Exitoso'),
        ('pendiente', 'Pendiente'),
        ('fallido', 'Fallido'),
    ]
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    estado_pago = models.CharField(max_length=20, choices=ESTADO_PAGO_CHOICES, default='pendiente')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    detalles = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Pago de Venta {self.venta.id}"
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='autos')

    def __str__(self):
        return f'{self.marca} {self.modelo}'

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class PersonaPerro(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.persona.nombre} - {self.perro.nombre}'
