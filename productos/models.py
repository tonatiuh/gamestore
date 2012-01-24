from django.forms import ModelForm
from django.db import models


class Producto(models.Model):
	nombre = models.CharField(max_length = 150)
	precio = models.DecimalField(max_digits = 8, decimal_places = 2)
	def __unicode__(self):
		return self.nombre

class ProductoForm(ModelForm):
	class Meta:
		model = Producto