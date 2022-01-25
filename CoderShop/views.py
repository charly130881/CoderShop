from xml.dom.expatbuilder import DOCUMENT_NODE
from django.http import HttpResponse
from django.shortcuts import redirect, render
from CoderShop.forms import VendedorForm, ClienteForm, ProductoForm
from CoderShop.models import Producto, Vendedor, Cliente

# Create your views here.

def inicio(request):
    
    return render(request, 'CoderShop/inicio.html')

def producto(request):
    
    return render(request, 'CoderShop/producto.html',
    {'producto': Producto.objects.all()})
    
def vendedor(request):
    
    return render(request, 'CoderShop/vendedor.html',
     {'vendedor': Vendedor.objects.all()})

def cliente(request):
    
    return render(request, 'CoderShop/cliente.html',
    {'cliente': Cliente.objects.all()})

def vendedorFormulario(request):
    if request.method == 'POST':
        
        formulario = VendedorForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            Vendedor.objects.create(nombre=data['nombre'], apellido=data['apellido'], legajo=data['legajo'])
            return redirect('Vendedor')
    else:
        formulario = VendedorForm()
       
    return render(request, "CoderShop/vendedorFormulario.html", {"formulario":formulario})

def productoFormulario(request):
    if request.method == 'POST':
        
        formulario = ProductoForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            Producto.objects.create(prenda=data['prenda'], codigo=data['codigo'], precio=data['precio'])
            return redirect('Producto')
    else:
        formulario = ProductoForm()
       
    return render(request, "CoderShop/productoFormulario.html", {"formulario":formulario})

def clienteFormulario(request):
    if request.method == 'POST':
        
        formulario = ClienteForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            Cliente.objects.create(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], telefono=data['telefono'])
            return redirect('Cliente')
    else:
        formulario = ClienteForm()
       
    return render(request, "CoderShop/clienteFormulario.html", {"formulario":formulario})

def buscarLegajo(request):
    
    return render(request, "CoderShop/buscarLegajo.html")

def buscar(request):
   
    if request.GET['legajo']:
        # respuesta = f"Estoy buscando el legajo nro.: {request.GET['legajo']}"
        legajo = request.GET['legajo']
    
        vendedor = Vendedor.objects.filter(legajo=legajo)
        
        return render(request, "CoderShop/buscar.html",
         {'vendedor':vendedor, 'legajo': legajo})
        
    else:
        respuesta = "No enviaste datos"
   
    # return HttpResponse(respuesta)
    return render(request, "CoderShop/inicio.html", {"respuesta":respuesta})


def buscarNombre(request):
    
    return render(request, "CoderShop/buscarNombre.html")

def buscar2(request):
   
    if request.GET['nombre']:
        # respuesta = f"Estoy buscando el legajo nro.: {request.GET['legajo']}"
        nombre = request.GET['nombre']
        
    
        vendedor = Vendedor.objects.filter(nombre=nombre)
        
        
        
        return render(request, "CoderShop/buscar2.html",
         {'vendedor':vendedor, 'nombre': nombre})
        
    else:
        respuesta = "No enviaste datos"
   
    # return HttpResponse(respuesta)
    return render(request, "CoderShop/inicio.html", {"respuesta":respuesta})