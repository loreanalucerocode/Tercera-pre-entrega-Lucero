from django.urls import path
from . import views  # Importa las vistas de tu aplicación

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),  
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('buscar/', views.buscar, name='buscar'),
    path('resultados_busqueda/', views.resultados_busqueda, name='resultados_busqueda'),  
]
