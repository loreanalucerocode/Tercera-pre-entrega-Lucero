from django import forms
from .models import Categoria, Producto, Pedido

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
