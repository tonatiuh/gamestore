from django.db import models
from clientes.models import Cliente
from almacen.models import Producto
from django.forms import ModelForm

class ApartadoDetail(models.Model):
	cliente = models.ForeignKey(Cliente)
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits = 3, decimal_places = 0)
	def __unicode__(self):
		return '['+str(self.cantidad)+']'+self.cliente.nombre+' '+self.cliente.primer_apellido

class ApartadoDetailForm(ModelForm):
	class Meta:
		model = ApartadoDetail

