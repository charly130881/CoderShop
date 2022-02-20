from multiprocessing import AuthenticationError
from pyexpat import model
from django.db import models
from django.contrib import messages
from xml.dom.expatbuilder import DOCUMENT_NODE
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import context
from CoderShop.forms import AvatarFormulario, UserRegisterForm, VendedorForm, ClienteForm, ProductoForm
from CoderShop.models import Avatar, Post, Producto, Vendedor, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, User
from django.contrib.auth import login, logout, authenticate, models
from CoderShop.forms import UserCreationForm, UserEditForm
# Create your views here.

class AvatarView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = Avatar.objects.filter(user=self.request.user.id).last().imagen.url
        return context



def welcomePage(request):
    
    return render(request, 'CoderShop/welcomePage.html')


def inicio(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
        
    return render(request, 'CoderShop/inicio.html', {'url':avatar_url})

@login_required
def producto(request):
    
    return render(request, 'CoderShop/producto.html',
    {'producto': Producto.objects.all()})
 
@login_required    
def vendedor(request):
    
    return render(request, 'CoderShop/vendedor.html',
    {'vendedor': Vendedor.objects.all()})

@login_required
def cliente(request):
    
    return render(request, 'CoderShop/cliente.html',
    {'cliente': Cliente.objects.all()})
    
@login_required
def post(request):
    
    return render(request, 'CoderShop/blog.html',
    {'post': Post.objects.all()})    
    
    

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

class VendedorListView(AvatarView, ListView):
    
    model = Vendedor
    template_name = 'CoderShop/vendedor.html'
    context_object_name = 'Vendedor'
    
class VendedorDetailView(AvatarView, DetailView):
    model = Vendedor
    template_name = 'CoderShop/ver_vendedor.html'
    
class VendedorCreateView(AvatarView, CreateView):
    model = Vendedor
    success_url = reverse_lazy('Vendedor')
    fields = ['nombre', 'apellido', 'legajo', 'imagen']    
    template_name = 'CoderShop/vendedorformulario.html'
    
class VendedorUpdateView(AvatarView, UpdateView):
    model = Vendedor
    success_url = reverse_lazy('Vendedor')
    fields = ['nombre', 'apellido', 'legajo', 'imagen']    
    template_name = 'CoderShop/vendedorformulario.html'  
      
class VendedorDeleteView(AvatarView, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('Vendedor')  
    template_name = 'CoderShop/vendedor_confirm_delete.html'  
    
# Clientes

class ClienteListView(LoginRequiredMixin, AvatarView, ListView):
    
    model = Cliente
    template_name = 'CoderShop/cliente.html'
    context_object_name = 'cliente'
    
class ClienteDetailView(AvatarView, DetailView):
    model = Cliente
    template_name = 'CoderShop/ver_cliente.html'
    
class ClienteCreateView(AvatarView, CreateView):
    model = Cliente
    success_url = reverse_lazy('cliente')
    fields = ['nombre', 'apellido', 'email', 'telefono']    
    template_name = 'CoderShop/clienteformulario.html'
    
class ClienteUpdateView(AvatarView, UpdateView):
    model = Cliente
    success_url = reverse_lazy('cliente')
    fields = ['nombre', 'apellido', 'email', 'telefono']    
    template_name = 'CoderShop/clienteformulario.html'  
      
class ClienteDeleteView(AvatarView, DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente')  
    template_name = 'CoderShop/cliente_confirm_delete.html'   
    
# Productos

class ProductoListView(AvatarView, ListView):
    
    model = Producto
    template_name = 'CoderShop/producto.html'
    context_object_name = 'producto'
    
class ProductoDetailView(AvatarView, DetailView):
    model = Producto
    template_name = 'CoderShop/ver_producto.html'
    
class ProductoCreateView(AvatarView, CreateView):
    model = Producto
    success_url = reverse_lazy('producto')
    fields = ['prenda', 'codigo', 'precio', 'imagen']    
    template_name = 'CoderShop/productoformulario.html'
    
class ProductoUpdateView(AvatarView, UpdateView):
    model = Producto
    success_url = reverse_lazy('producto')
    fields = ['prenda', 'codigo', 'precio', 'imagen']    
    template_name = 'CoderShop/productoformulario.html'  
      
class ProductoDeleteView(AvatarView, DeleteView):
    model = Producto
    success_url = reverse_lazy('producto')  
    template_name = 'CoderShop/producto_confirm_delete.html'

# Login

# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
        
#         if form.is_valid():
#             usuario = form.cleaned_data['username']
#             password = form.cleaned_data['password']            
#             user = authenticate(username=usuario, password=password)
            
#             if user is not None:
#                 login(request, user) 
#                 return redirect('Inicio')               
#             else:
#                 return render(request, 'CoderShop/login.html',
#                         {'form': form, 
#                         'error': 'No es válido el usuario y contraseña'})            
#         else:
#             return render(request, 'CoderShop/login.html', {'form': form})    
#     else:
#         form = AuthenticationForm()       
#         return render(request, 'CoderShop/login.html', {'form': form})
    
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
            
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             form.save()
#             messages.success(request, f'Usuario {username} creado con éxito!')
#             return redirect('Inicio')
#     else:
#             form = UserRegisterForm()  
           
#             return render(request, 'CoderShop/register.html', {'form' : form })
        
class UserCreateView(CreateView)  :
    model = User  
    # succes_url = reverse_lazy('login.html')
    template_name = 'register.html'
    form_class = UserRegisterForm
    def get_success_url(self):
        return reverse('login')

@login_required       
def editarUsuario(request):
    usuario = request.user

    
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            usuario.email = data['email']
            usuario.set_password = data['password1']
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.save()
            
            return render(request, 'CoderShop/Inicio.html')
    
    else:
        formulario = UserEditForm(initial={'email':usuario.email})
            
    return render(request, 'CoderShop/editarUsuario.html', {'formulario':formulario, 'usuario':usuario})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            return redirect('Inicio')
    
    else:
        form = AvatarFormulario()
    return render(request, 'CoderShop/agregarAvatar.html', {'form':form})     

# Blog

class BlogListView(AvatarView, ListView):
    model = Post
    template_name ='CoderShop/blog.html'
    context_object_name = 'post'
    
class BlogCreateView(AvatarView, CreateView):
    model = Post
    success_url = reverse_lazy('post')
    fields = ['titulo', 'descripcion', 'contenido', 'publicado', 'autor', 'estado']    
    template_name = 'CoderShop/postformulario.html'  
    
class BlogDetailView(AvatarView, DetailView):
    model = Post
    template_name = 'CoderShop/ver_post.html'   
     
class BlogUpdateView(AvatarView, UpdateView):
    model = Post
    success_url = reverse_lazy('post')
    fields = ['titulo', 'descripcion', 'contenido', 'publicado', 'autor', 'estado']    
    template_name = 'CoderShop/postformulario.html'
    
class BlogDeleteView(AvatarView, DeleteView):
    model = Post
    success_url = reverse_lazy('post')
    template_name = 'CoderShop/post_confirm_delete.html'         
    
 
    
    



  

