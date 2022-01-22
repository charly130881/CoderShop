from django.db import models

# Create your models here.
class Productos(models.Model):
    
    nombre=models.CharField(max_length=30)
    codigo = models.IntegerField()
    precio = models.IntegerField()
    
class Vendedores(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo = models.IntegerField()
    
class Clientes(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido = models.CharField(max_length=30) 
    email = models.EmailField(30)    
    telefono = models.IntegerField(30)