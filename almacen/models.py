from django.forms import ModelForm
from django.db import models
from productos.models import Producto

class Almacenado(models.Model):
	producto = models.ForeignKey(Producto)
	codigo = models.IntegerField(unique = True)
	def __unicode__(self):
		return str(self.codigo)
	def total(self):
		total = Almacenado.objects.filter(producto__id = self.producto.id).count()
		return total


class AlmacenadoForm(ModelForm):
	class Meta:
		model = Almacenado