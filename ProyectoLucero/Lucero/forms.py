from django import forms
from .models import Categoria, Producto, Pedido
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre'] 

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)


from django import forms
from .models import Avatar

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']  
        labels = {
            'imagen': 'Avatar'  # Etiqueta personalizada para el campo 'imagen'
        }

from django import forms
from .models import Imagen  # Asegúrate de importar el modelo Imagen

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['titulo', 'imagen', 'descripcion']


from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class MyPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User  # Reemplaza 'User' con tu modelo de usuario personalizado si lo tienes
