from django.urls import path
from CoderShop import views
from CoderShop.views import inicio, productos, vendedores, clientes


urlpatterns = [
    
    path('', views.inicio),
    path('productos', views.productos),
    path('vendedores', views.vendedores),
    path('clientes', views.clientes),
    
    
]         
         