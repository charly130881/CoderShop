from xml.dom.expatbuilder import DOCUMENT_NODE
from django.http import HttpResponse
from django.shortcuts import redirect, render
from CoderShop.forms import VendedorForm, ClienteForm
from CoderShop.models import Productos, Vendedor, Cliente

# Create your views here.
def inicio(request):
    
    return render(request, 'CoderShop/inicio.html')

def productos(request):
    
    return render(request, 'CoderShop/productos.html')
    
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
    
    # respuesta = f"Estoy buscando el legajo nro.: {request.GET['legajo']}"
    legajo = request.GET['legajo']
    
    vendedor = Vendedor.objects.filter(legajo=legajo)
        
    return render(request, "CoderShop/buscar.html",
    {'vendedor':vendedor, 'legajo': legajo})
    # else:
    #     respuesta = "No enviaste datos"
   
    # return HttpResponse(respuesta)