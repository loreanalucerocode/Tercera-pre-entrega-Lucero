# Lucero Store

Lucero Store es una aplicación web desarrollada con Django que te permite administrar categorías y productos. También puedes buscar productos en la base de datos.

## Modelos

### Categoría

El modelo `Categoría` representa las categorías de productos disponibles en la tienda. Cada categoría tiene los siguientes campos:

- `nombre`: El nombre de la categoría (por ejemplo, "Electrónica").
- `descripcion`: Una breve descripción de la categoría.

### Producto

El modelo `Producto` representa los productos disponibles en la tienda. Cada producto tiene los siguientes campos:

- `nombre`: El nombre del producto (por ejemplo, "Smartphone").
- `descripcion`: Una breve descripción del producto.
- `precio`: El precio del producto.
- `categoria`: Una relación con la categoría a la que pertenece el producto.

## Requisitos

- Python 3.x
- Django 4.2.x


