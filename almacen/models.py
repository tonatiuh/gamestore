from django.forms import ModelForm
from django.db import models
from productos.models import Producto

class AlmacenDetail(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits = 3, decimal_places = 0)
	def __unicode__(self):
		return self.producto.nombre

class AlmacenDetailForm(ModelForm):
	class Meta:
		model = AlmacenDetail
