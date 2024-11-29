from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Empleado(models.Model):
    ROLES = [
        ('admin' , 'Administrador'),
        ('empleado' , 'Empleado'),
    ]
    nombre = models.CharField( max_length=1000)
    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')
    correo = models.EmailField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo  = models.EmailField(unique=True)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


