
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    direccion = models.TextField(max_length=150, verbose_name='Dirección', blank=True)
    email = models.EmailField(max_length=100, verbose_name='Email')
    password = models.CharField(max_length=10, verbose_name='Password')

    def __str__(self):
        return self.username


class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción',blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    cantidad = models.IntegerField(verbose_name='Cantidad')

    def __str__(self):
        return self.nombre

