from xml.dom.expatbuilder import DOCUMENT_NODE
from django.http import HttpResponse
from django.shortcuts import render

from CoderShop.models import Productos

# Create your views here.
def producto(request):
    
    producto = Productos(nombre="Remera", codigo=4334, precio=1500)
    producto.save()
    documentoDeTexto = f"--->Producto: {producto.nombre} codigo: {producto.codigo} precio: {producto.precio}"
    
    return HttpResponse(documentoDeTexto)