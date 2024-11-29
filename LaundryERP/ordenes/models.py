from django.db import models
from usuarios.models import Cliente, Empleado

# Create your models here.
class Prenda(models.Model):
    tipo_prenda = models.CharField(max_length=50)
    precio  = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.tipo_prenda
    
class OrdenDeServicio(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('proceso', 'En Proceso'),
        ('completada', 'Completada'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prendas  = models.ManyToManyField(Prenda)
    fecha_creacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='pendiente')
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    pago_realizado = models.BooleanField(default=False)
    
    def calcular_total(self):
        self.total = sum(prenda.precio for prenda in self.prendas.all())
        self.save()
    
    def __str__(self):
        return f'Orden #{self.id} - {self.cliente.nombre} - {self.estado} - {self.total}'
    
    