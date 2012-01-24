from django.forms import ModelForm
from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length = 150)
	primer_apellido =  models.CharField(max_length = 150)
	segundo_apellido = models.CharField(max_length = 150)
	telefono = models.CharField(max_length = 10)
	def __unicode__(self):
		return self.nombre

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente

"""
class Producto(models.Model):
	nombre = models.CharField(max_length = 150)
	precio = models.DecimalField(max_digits = 8, decimal_places = 2)
	def __unicode__(self):
		return self.nombre

class ProductoForm(ModelForm):
	class Meta:
		model = Producto



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
"""