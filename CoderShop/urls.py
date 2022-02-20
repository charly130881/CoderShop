from django.urls import path
from CoderShop import views
from CoderShop.views import BlogDeleteView, BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView, ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDeleteView, ClienteDetailView, UserCreateView, VendedorCreateView, VendedorListView, VendedorUpdateView, VendedorDeleteView, VendedorDetailView, agregarAvatar, buscar, buscarNombre, cliente, inicio, producto, vendedor, clienteFormulario, buscarLegajo, productoFormulario, buscar2, welcomePage, editarUsuario
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    
    path('', welcomePage, name="WelcomePage"),
    path('inicio', inicio, name="Inicio"),
    # Busqueda
    path('buscarLegajo', buscarLegajo, name="BuscarLegajo"),
    path('buscar', buscar, name="buscar"), 
    path('buscarNombre', buscarNombre, name="buscarNombre"),
    path('buscar2', buscar2, name="buscar2"),  
    # Vendedor
    path('vendedor', VendedorListView.as_view(), name="Vendedor"),
    path('vendedor/detail/<pk>', VendedorDetailView.as_view(), name="ver_vendedor"),
    path('vendedorFormulario', VendedorCreateView.as_view(), name="vendedorFormulario"),
    path('vendedor/update/<pk>', VendedorUpdateView.as_view(), name='vendedor_update'),
    path('vendedor/delete/<pk>', VendedorDeleteView.as_view(), name='vendedor_confirm_delete'),
    # Cliente
    path('cliente', ClienteListView.as_view(), name="cliente"),
    path('cliente/detail/<pk>', ClienteDetailView.as_view(), name="ver_cliente"),
    path('clienteFormulario', ClienteCreateView.as_view(), name="clienteFormulario"),
    path('cliente/update/<pk>', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/delete/<pk>', ClienteDeleteView.as_view(), name='cliente_confirm_delete'),
    # Producto
    path('producto', ProductoListView.as_view(), name="producto"),
    path('producto/detail/<pk>', ProductoDetailView.as_view(), name="ver_producto"),
    path('productoFormulario', ProductoCreateView.as_view(), name="productoFormulario"),
    path('producto/update/<pk>', ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/delete/<pk>', ProductoDeleteView.as_view(), name='producto_confirm_delete'),
    # Login
    path('login', LoginView.as_view(template_name='CoderShop/login.html'), name='login'),   
    path('register', UserCreateView.as_view(template_name='CoderShop/register.html'), name='register'), 
    path('logout', LogoutView.as_view(template_name='CoderShop/logout.html'), name='logout'),
    path('editarUsuario', editarUsuario, name='editarUsuario'),
    path('agregarAvatar', agregarAvatar, name='agregarAvatar'),
    # Blog
    path('post', BlogListView.as_view(), name='post'),
    path('post/detail/<pk>', BlogDetailView.as_view(), name="ver_post"),
    path('postFormulario', BlogCreateView.as_view(), name="postFormulario"),
    path('postFormulario/update/<pk>', BlogUpdateView.as_view(), name="post_update"),
    path('post/delete/<pk>', BlogDeleteView.as_view(), name='post_confirm_delete'),
    
    
   
]
    




         
         