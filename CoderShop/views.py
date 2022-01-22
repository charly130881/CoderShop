from xml.dom.expatbuilder import DOCUMENT_NODE
from django.http import HttpResponse
from django.shortcuts import render

from CoderShop.models import Productos

# Create your views here.
def inicio(request):
    
    return render(request, 'CoderShop/inicio.html')

def productos(request):
    
    return render(request, 'CoderShop/productos.html')
    
def vendedores(request):
    
    return render(request, 'CoderShop/vendedores.html')

def clientes(request):
    
    return render(request, 'CoderShop/clientes.html') 