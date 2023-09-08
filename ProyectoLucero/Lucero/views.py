from django.shortcuts import render, redirect
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm, BusquedaForm
from .forms import PedidoForm
from django.shortcuts import render

def pagina_inicio(request):
    return render(request, 'Lucero/base.html')

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_inicio')  # Redirige a la página principal después de guardar
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

def resultados_busqueda(request):
    return render(request, 'Lucero/resultados_busqueda.html', {})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('pagina_de_exito_producto')
    else:
        form = ProductoForm()
    return render(request, 'Lucero/crear_producto.html', {'form': form})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return redirect('pagina_de_exito_pedido')
    else:
        form = PedidoForm()
    return render(request, 'Lucero/crear_pedido.html', {'form': form})

def pagina_de_exito_producto(request):
    return render(request,'Lucero/pagina_de_exito_producto.html')

def pagina_de_exito_pedido(request):
    return render(request, 'Lucero/pagina_de_exito_pedido.html')
