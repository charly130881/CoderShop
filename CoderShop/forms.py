import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}
        
    
    
    
           