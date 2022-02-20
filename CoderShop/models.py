

from email.policy import default
from django.utils import timezone
from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Producto(models.Model):
    
    prenda = models.CharField(max_length=30)
    codigo = models.IntegerField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return f'* Prenda: {self.prenda} | Código: {self.codigo} | Precio: $ {self.precio}'
    
class Vendedor(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo = models.IntegerField()
    imagen = models.ImageField(upload_to="vendedores", null=True)
    
    
    def __str__(self):
        return f'* Vendedor/a: {self.nombre} {self.apellido} | Legajo: {self.legajo}'
    
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30) 
    email = models.EmailField()    
    telefono = models.IntegerField()
    
    def __str__(self):
        return f'* Cliente: {self.nombre} {self.apellido} | e-mail: {self.email} | Teléfono: {self.telefono}'
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f'* Usuario: {self.user} | imagen: {self.imagen}'
    
# Blog

# # class Categoria(models.Model):
    
#     nombre = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.nombre

class Post(models.Model):
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(estado='publicado')
    
    
    
    opciones = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )    
    
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    contenido = models.TextField(null=True)
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=opciones, default='borrador')     
    objects = models.Manager()
    postobjects = PostObjects()
    
    class Meta:
        ordering = ('-publicado',)      
    
    
    def __str__(self):
            return self.titulo  
        
    
    
    
    
         
          
        

# class Comentarios(models.Model):
    
#     post = models.ForeignKey(on_delete=models.CASCADE, related_name='comentarios')
#     nombre = models.CharField(max_length=55)
#     email = models.EmailField()
#     Contentenido = models.TextField
#     publicado = models.DateTimeField(auto_now_add=True)
#     estado = models.BooleanField(default=True)  
    
#     class Meta:
#         ordering = ("publicado",)
        
#         def __str__(self):
#             return f"Comentario de {self.nombre}"    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        