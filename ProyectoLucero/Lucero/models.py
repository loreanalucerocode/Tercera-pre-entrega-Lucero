from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class ClaseQueNecesitaLogin(LoginRequiredMixin, View):
    def get(self, request):
        datos = {'mensaje': 'Hola debe ingresar:'}
        return render(request, 'login.html')

from django.contrib.auth.models import User
from django.db import models

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

from django.db import models

class Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='media/', null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
