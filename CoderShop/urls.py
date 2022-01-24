from django.urls import path
from CoderShop import views
from CoderShop.views import buscar, cliente, inicio, producto, vendedor, vendedorFormulario, clienteFormulario, buscarLegajo, productoFormulario


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
    
    
]         
         