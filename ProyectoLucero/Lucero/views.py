from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm, BusquedaForm
from .forms import PedidoForm
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View


def pagina_inicio(request):
    return render(request, 'Lucero/base.html')


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_inicio')  
    else:
        form = CategoriaForm()
    return render(request, 'Lucero/crear_categoria.html', {'form': form})

from django.http import JsonResponse

from django.shortcuts import render
from .models import Producto  # Importa el modelo de Producto

from django.shortcuts import render
from .models import Producto  # Importa el modelo de Producto
from django.http import JsonResponse  # Importa JsonResponse para devolver datos en formato JSON

from django.shortcuts import render
from .models import Producto

def buscar_productos(request):
    resultados = None  # Inicializamos la variable de resultados como None

    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        termino_busqueda = request.POST.get('termino_busqueda', '')

        # Realizar la consulta para obtener productos únicos por nombre
        resultados = Producto.objects.filter(nombre__icontains=termino_busqueda).values('nombre').distinct()

    return render(request, 'Lucero/buscar.html', {'resultados': resultados})



def resultados_busqueda(request):
    return render(request, 'Lucero/resultados_busqueda.html', {})

from django.shortcuts import render, redirect
from .forms import ProductoForm

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            # No redirigir, simplemente mostrar un mensaje de éxito en la misma página
            return render(request, 'Lucero/crear_producto.html', {'form': form, 'exito': True})
    else:
        form = ProductoForm()
    return render(request, 'Lucero/crear_producto.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import PedidoForm

def crear_pedido(request):
    mensaje_exito = None  # Inicialmente, no hay mensaje de éxito

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            mensaje_exito = 'Pedido realizado con éxito!' 
    else:
        form = PedidoForm()

    return render(request, 'Lucero/crear_pedido.html', {'form': form, 'mensaje_exito': mensaje_exito})


from django.core.exceptions import MultipleObjectsReturned

from django.core.exceptions import MultipleObjectsReturned


@login_required
def leer_categoria(request, nombre_categoria):
    categorias = Categoria.objects.all() 
    contexto = {"categorias": categorias} 
    return render(request, "Lucero/leer_categoria.html", contexto)




from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import get_object_or_404, redirect


from django.shortcuts import render, redirect
from Lucero.models import Categoria

from django.shortcuts import render, redirect
from Lucero.models import Categoria
import logging

from django.shortcuts import get_object_or_404, redirect

@login_required
def eliminar_categoria(request, nombre_categoria):
    categoria = get_object_or_404(Categoria, nombre=nombre_categoria)

    if request.method == 'POST':
        categoria.delete()
        return redirect('pagina_inicio')  # Redirige a la página de inicio o a donde desees después de eliminar

    return render(request, 'Lucero/eliminar_categoria.html', {'categoria': categoria})



       
def editar_categoria(request, nombre_categoria):
    categoria = get_object_or_404(Categoria, nombre=nombre_categoria)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            # Redirige a la vista leer_categoria con el nombre de la categoría
            return redirect('leer_categoria', nombre_categoria=nombre_categoria)
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'Lucero/editar_categoria.html', {'form': form, 'categoria': categoria})



from django.contrib import messages

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            # Redirige al usuario al inicio de la plataforma
            return redirect('pagina_inicio')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    
    return render(request, 'Lucero/login.html')


def register(request):

    if request.method== 'POST' :

        form = UserCreationForm(request.POST)

        if form.is_valid():
            usenrname= form.cleaned_data['username']
            form.save()
            return render(request,'Lucero/base.html',{'mensaje':'Usuario creado:) '})

    else: 
        form= UserCreationForm()

    return render(request,'Lucero/registro.html', {'form':form })



from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required
from .models import Avatar
from .forms import UserChangeForm, PasswordChangeForm, AvatarForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Avatar
from .forms import UserChangeForm, PasswordChangeForm, AvatarForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Avatar
from .forms import UserChangeForm, PasswordChangeForm, AvatarForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Avatar
from .forms import UserChangeForm, AvatarForm
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import MyPasswordChangeForm  # Importa el nuevo formulario

@login_required
def EditarPerfil(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        password_form = MyPasswordChangeForm(request.user, request.POST)  # Usa el nuevo formulario

        if user_form.is_valid() and avatar_form.is_valid() and password_form.is_valid():
            user_form.save()
            if avatar_form.cleaned_data['imagen']:
                if avatar:
                    avatar.imagen = avatar_form.cleaned_data['imagen']
                else:
                    avatar = Avatar(user=request.user, imagen=avatar_form.cleaned_data['imagen'])
                avatar.save()
            elif avatar:
                avatar.delete()
            
            # Cambia la contraseña si el formulario de cambio de contraseña es válido
            password_form.save()
            
            messages.success(request, 'Tu perfil y contraseña han sido actualizados con éxito.')
            return redirect('pagina_inicio')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        user_form = UserChangeForm(instance=request.user)
        avatar_form = AvatarForm(instance=avatar)
        password_form = MyPasswordChangeForm(request.user)  # Usa el nuevo formulario

    return render(request, 'Lucero/EditarPerfil.html', {'user_form': user_form, 'avatar_form': avatar_form, 'avatar': avatar, 'password_form': password_form})

def mensaje_no_autenticado(request):
    messages.warning(request, 'Debes iniciar sesión o registrarte para editar tu perfil.')
    return redirect('pagina_inicio')  

def about(request):
    return render(request, 'Lucero/about.html')


