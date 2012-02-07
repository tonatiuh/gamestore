from django.db import models
from clientes.models import Cliente
from productos.models import Producto
from django.forms import ModelForm

class Cotizacion(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	cliente = models.ForeignKey(Cliente)
	def __unicode__(self):
		return '['+str(self.fecha.day)+'/'+str(self.fecha.month)+'/'+str(self.fecha.year)+']  '+self.cliente.nombre+' '+self.cliente.primer_apellido 
	def total(self):
		cotizaciondetails = CotizacionDetail.objects.filter(cotizacion__id__exact = self.id)
		total = 0
		for cotizaciondetail in cotizaciondetails:
			total += cotizaciondetail.cantidad * cotizaciondetail.producto.precio
		return total

class CotizacionDetail(models.Model):
	cotizacion = models.ForeignKey(Cotizacion)
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits = 5, decimal_places = 2)
	def total(self):
		total = self.cantidad * self.producto.precio
		return total


class CotizacionForm(ModelForm):
	class Meta:
		model = Cotizacion

class CotizacionDetailForm(ModelForm):
	class Meta:
		model = CotizacionDetail