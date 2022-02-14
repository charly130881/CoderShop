from multiprocessing import AuthenticationError
from pyexpat import model
from django.contrib import messages
from xml.dom.expatbuilder import DOCUMENT_NODE
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import context
from CoderShop.forms import UserRegisterForm, VendedorForm, ClienteForm, ProductoForm
from CoderShop.models import Producto, Vendedor, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, User
from django.contrib.auth import login, logout, authenticate
from CoderShop.forms import UserCreationForm
# Create your views here.

def welcomePage(request):
    
    return render(request, 'CoderShop/welcomePage.html')

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

# def vendedorFormulario(request):
#     if request.method == 'POST':
        
#         formulario = VendedorForm(request.POST)
        
#         if formulario.is_valid():
#             data = formulario.cleaned_data
#             Vendedor.objects.create(nombre=data['nombre'], apellido=data['apellido'], legajo=data['legajo'])
#             return redirect('Vendedor')
#     else:
#         formulario = VendedorForm()
       
#     return render(request, "CoderShop/vendedorFormulario.html", {"formulario":formulario})

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
            return redirect('cliente')
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





# def vendedor_delete(request, vendedor_id):
    
#     vendedor = Vendedor.objects.get(id=vendedor_id)
#     vendedor.delete()
#     # vendedor = Vendedor.objects.all()
    
    
    
    
#     return redirect('Vendedor')

# def vendedor_update(request, vendedor_id):
#     vendedor = Vendedor.objects.get(id=vendedor_id)
    
#     if request.method == 'POST':
        
#         formulario = VendedorForm(request.POST)
        
#         if formulario.is_valid():
#             data = formulario.cleaned_data
            
#             vendedor.nombre = data['nombre']
#             vendedor.apellido = data['apellido']
#             vendedor.legajo = data['legajo']
#             vendedor.save()
            
#             return redirect('Vendedor')
#     else:
#         formulario = VendedorForm(model_to_dict(vendedor))
       
#     return render(request, "CoderShop/vendedorFormulario.html", {"formulario":formulario})


# Vendedores

class VendedorListView(ListView):
    
    model = Vendedor
    template_name = 'CoderShop/vendedor.html'
    context_object_name = 'Vendedor'
    
class VendedorDetailView(DetailView):
    model = Vendedor
    template_name = 'CoderShop/ver_vendedor.html'
    
class VendedorCreateView(CreateView):
    model = Vendedor
    success_url = reverse_lazy('Vendedor')
    fields = ['nombre', 'apellido', 'legajo']    
    template_name = 'CoderShop/vendedorformulario.html'
    
class VendedorUpdateView(UpdateView):
    model = Vendedor
    success_url = reverse_lazy('Vendedor')
    fields = ['nombre', 'apellido', 'legajo']    
    template_name = 'CoderShop/vendedorformulario.html'  
      
class VendedorDeleteView(DeleteView):
    model = Vendedor
    success_url = reverse_lazy('Vendedor')  
    template_name = 'CoderShop/vendedor_confirm_delete.html'  
    
# Clientes

class ClienteListView(ListView):
    
    model = Cliente
    template_name = 'CoderShop/cliente.html'
    context_object_name = 'cliente'
    
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'CoderShop/ver_cliente.html'
    
class ClienteCreateView(CreateView):
    model = Cliente
    success_url = reverse_lazy('cliente')
    fields = ['nombre', 'apellido', 'email', 'telefono']    
    template_name = 'CoderShop/clienteformulario.html'
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    success_url = reverse_lazy('cliente')
    fields = ['nombre', 'apellido', 'email', 'telefono']    
    template_name = 'CoderShop/clienteformulario.html'  
      
class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente')  
    template_name = 'CoderShop/cliente_confirm_delete.html'   
    
# Productos

class ProductoListView(ListView):
    
    model = Producto
    template_name = 'CoderShop/producto.html'
    context_object_name = 'producto'
    
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'CoderShop/ver_producto.html'
    
class ProductoCreateView(CreateView):
    model = Producto
    success_url = reverse_lazy('producto')
    fields = ['prenda', 'codigo', 'precio']    
    template_name = 'CoderShop/productoformulario.html'
    
class ProductoUpdateView(UpdateView):
    model = Producto
    success_url = reverse_lazy('producto')
    fields = ['prenda', 'codigo', 'precio']    
    template_name = 'CoderShop/productoformulario.html'  
      
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto')  
    template_name = 'CoderShop/producto_confirm_delete.html'

# Login

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password']            
            user = authenticate(username=usuario, password=password)
            
            if user is not None:
                login(request, user) 
                return redirect('Inicio')               
            else:
                return render(request, 'CoderShop/login.html',
                        {'form': form, 
                        'error': 'No es válido el usuario y contraseña'})            
        else:
            return render(request, 'CoderShop/login.html', {'form': form})    
    else:
        form = AuthenticationForm()       
        return render(request, 'CoderShop/login.html', {'form': form})
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
            
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Usuario {username} creado con éxito!')
            return redirect('Inicio')
    else:
            form = UserRegisterForm()  
           
    return render(request, 'CoderShop/register.html', {'form' : form })