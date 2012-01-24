from productos.models import Producto
from clientes.models import Cliente
from django.forms import ModelForm
from django.db import models

class Venta(models.Model):
	cliente = models.ForeignKey(Cliente)
	fecha = models.DateTimeField()

class Venta_description(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits = 3, decimal_places = 0)
	venta = models.ForeignKey(Venta)

class VentaForm(ModelForm):
	class Meta:
		model = Venta