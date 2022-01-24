from django import forms

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