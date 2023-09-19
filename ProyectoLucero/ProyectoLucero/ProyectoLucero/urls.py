from django.contrib import admin
from django.urls import path, include
from Lucero.views import pagina_inicio, crear_categoria, buscar, resultados_busqueda
from django.conf import settings
from django.conf import static

urlpatterns = [
    path('', include('Lucero.urls')),  
    path('admin/', admin.site.urls),
   
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
