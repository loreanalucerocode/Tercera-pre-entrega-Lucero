from django.contrib import admin
from django.urls import path, include
from Lucero.views import (
    pagina_inicio, crear_categoria, buscar, resultados_busqueda,
    crear_pedido, crear_producto, pagina_de_exito_producto,pagina_de_exito_pedido
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', pagina_inicio, name='pagina_inicio'), 
    path('admin/', admin.site.urls),
    path('crear_categoria/', crear_categoria, name='crear_categoria'),
    path('buscar/', buscar, name='buscar'), 
    path('resultados_busqueda/', resultados_busqueda, name='resultados_busqueda'), 
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('pagina_de_exito_producto/', pagina_de_exito_producto, name='pagina_de_exito_producto'),
     path('pagina_de_exito_pedido/', pagina_de_exito_pedido, name='pagina_de_exito_pedido'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
