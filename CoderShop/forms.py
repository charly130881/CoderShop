
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField, Form, ImageField, PasswordInput


class VendedorForm(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    legajo = forms.IntegerField()
    
    
class ClienteForm(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()    
    telefono = forms.IntegerField()

class ProductoForm(forms.Form):
    
    prenda = forms.CharField()
    codigo = forms.IntegerField()
    precio = forms.IntegerField() 
    
class UserRegisterForm(UserCreationForm):
    
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    first_name = CharField(label='Nombre/s', widget=forms.TextInput)
    last_name = CharField(label='Apellido/s', widget=forms.TextInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
   
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=forms.PasswordInput)   
    first_name = CharField(label='Nombre/s', widget=forms.TextInput)
    last_name = CharField(label='Apellido/s', widget=forms.TextInput)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k:"" for k in fields} 

class AvatarFormulario(Form):
    imagen = ImageField(required=True)           