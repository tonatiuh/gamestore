from django.db import models
from django.forms import ModelForm
from productos.models import Producto

class Producto(models.Model):
	producto = models.ForeignKey(Producto, related_name = 'productoProveedor') #related_name to avoid the clash
	precio = models.DecimalField(max_digits = 9, decimal_places = 2)

class ProductoForm(ModelForm):
	class Meta:
		model = Producto

class Proveedor(models.Model):
	nombre = models.CharField(max_length = 30)
	def __unicode__(self):
		return self.nombre

class ProveedorForm(ModelForm):
	class Meta:
		model = Proveedor