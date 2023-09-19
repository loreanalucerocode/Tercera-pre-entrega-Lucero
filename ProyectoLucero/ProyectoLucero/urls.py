from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from Lucero.views import (
    crear_categoria, buscar_productos, resultados_busqueda,
    crear_pedido, crear_producto, leer_categoria, 
    eliminar_categoria, editar_categoria, login_request, register, LogoutView, pagina_inicio,EditarPerfil,about,
  
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_categoria/', crear_categoria, name='crear_categoria'),
    path('buscar_productos/', buscar_productos, name='buscar_productos'), 
    path('resultados_busqueda/', resultados_busqueda, name='resultados_busqueda'), 
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('leer_categoria/<str:nombre_categoria>/', leer_categoria, name='leer_categoria'),
    path('eliminar_categoria/<str:nombre_categoria>/', eliminar_categoria, name="eliminar_categoria"),
    path('editar_categoria/<str:nombre_categoria>/', editar_categoria, name='editar_categoria'),
    path('login/', login_request, name="login"),
    path('register/', register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='Lucero/logout.html'), name='logout'),
    path('', pagina_inicio, name='pagina_inicio'),
    path('EditarPerfil/', EditarPerfil, name='EditarPerfil'),
    path('about/', about, name='about')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
