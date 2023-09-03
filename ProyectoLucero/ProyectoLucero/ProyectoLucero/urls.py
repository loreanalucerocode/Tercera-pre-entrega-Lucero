from django.contrib import admin
from django.urls import path, include
from Lucero.views import pagina_inicio, crear_categoria, buscar, resultados_busqueda

urlpatterns = [
    path('', include('Lucero.urls')),  # Incluye las URLs de la aplicación "Lucero"
    path('admin/', admin.site.urls),
]
