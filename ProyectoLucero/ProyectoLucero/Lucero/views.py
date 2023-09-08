from django.shortcuts import render
from .models import Categoria, Producto, Pedido
from .forms import CategoriaForm, ProductoForm, BusquedaForm
from django.http import HttpResponse

def pagina_inicio(request):
    return render(request, 'Lucero/base.html')

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("La categoría se ha creado con éxito.")
    else:
        form = CategoriaForm()
    return render(request, 'Lucero/crear_categoria.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino_busqueda']
            resultados = Producto.objects.filter(nombre__icontains=termino)
            return render(request, 'Lucero/resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'Lucero/buscar.html', {'form': form})

# Agrega la vista resultados_busqueda
def resultados_busqueda(request):
    return render(request, 'Lucero/resultados_busqueda.html', {})
