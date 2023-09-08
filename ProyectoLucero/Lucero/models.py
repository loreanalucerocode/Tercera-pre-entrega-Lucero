from django.db import models


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
