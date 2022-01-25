from django.urls import path
from CoderShop import views
from CoderShop.views import buscar, buscarNombre, cliente, inicio, producto, vendedor, vendedorFormulario, clienteFormulario, buscarLegajo, productoFormulario, buscar2


urlpatterns = [
    
    path('', inicio, name="Inicio"),
    path('producto', producto, name="Producto"),
    path('vendedor', vendedor, name="Vendedor"),
    path('cliente', cliente, name="Cliente"),
    path('vendedorFormulario', vendedorFormulario, name="vendedorFormulario"),
    path('clienteFormulario', clienteFormulario, name="clienteFormulario"),
    path('productoFormulario', productoFormulario, name="productoFormulario"),
    path('buscarLegajo', buscarLegajo, name="BuscarLegajo"),
    path('buscar', buscar, name="buscar"), 
    path('buscarNombre', buscarNombre, name="buscarNombre"),
    path('buscar2', buscar2, name="buscar2"),   
]         
         