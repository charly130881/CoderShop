from django.db import models

# Create your models here.
class Producto(models.Model):
    
    prenda = models.CharField(max_length=30)
    codigo = models.IntegerField()
    precio = models.IntegerField()
    
    def __str__(self):
        return f'Producto {self.prenda} {self.codigo} {self.precio}'
    
class Vendedor(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo = models.IntegerField()
    
    def __str__(self):
        return f'Vendedor {self.nombre} {self.apellido} {self.legajo}'
    
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30) 
    email = models.EmailField(30)    
    telefono = models.IntegerField()
    
    def __str__(self):
        return f'Cliente {self.nombre} {self.apellido} {self.email} {self.telefono}'
    
    