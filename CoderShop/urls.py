from django.urls import path
from CoderShop import views
from CoderShop.views import buscar, cliente, inicio, productos, vendedor, vendedorFormulario, clienteFormulario, buscarLegajo


urlpatterns = [
    
    path('', inicio, name="Inicio"),
    path('productos', productos, name="Productos"),
    path('vendedor', vendedor, name="Vendedor"),
    path('cliente', cliente, name="Cliente"),
    path('vendedorFormulario', vendedorFormulario, name="vendedorFormulario"),
    path('clienteFormulario', clienteFormulario, name="clienteFormulario"),
    path('buscarLegajo', buscarLegajo, name="BuscarLegajo"),
    path('buscar', buscar, name="buscar"),
    
    
]         
         