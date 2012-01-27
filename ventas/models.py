from productos.models import Producto
from clientes.models import Cliente
from django.forms import ModelForm
from django.db import models

class Venta(models.Model):
	cliente = models.ForeignKey(Cliente)
	fecha = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return '['+str(self.fecha.day)+'/'+str(self.fecha.month)+'/'+str(self.fecha.year)+']  '+self.cliente.nombre+' '+self.cliente.primer_apellido 

class VentaForm(ModelForm):
	class Meta:
		model = Venta

class VentaDetail(models.Model):
	id = models.AutoField(primary_key=True)
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits = 3, decimal_places = 0)
	venta = models.ForeignKey(Venta)
	def __unicode__(self):
		return '['+str(self.cantidad)+'] '+self.producto.nombre
	class Meta:
		unique_together = (("producto", "venta"),)

class VentaDetailForm(ModelForm):
	class Meta:
		model = VentaDetail
		exclude = ('venta',)