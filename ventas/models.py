from almacen.models import Producto
from clientes.models import Cliente
from descuentos.models import Descuento
from django.forms import ModelForm
from django.db import models

class Venta(models.Model):
	cliente = models.ForeignKey(Cliente)
	fecha = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return '['+str(self.fecha.day)+'/'+str(self.fecha.month)+'/'+str(self.fecha.year)+']  '+self.cliente.nombre+' '+self.cliente.primer_apellido 
	def total(self):
		ventadetails = VentaDetail.objects.filter(venta__id__exact = self.id)
		total = 0
		for ventadetail in ventadetails:
			total += ventadetail.cantidad * ventadetail.producto.producto.precio
		return total
	def test():
		return 2

class VentaForm(ModelForm):
	class Meta:
		model = Venta

class VentaDetail(models.Model):
	id = models.AutoField(primary_key=True)
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits = 3, decimal_places = 0)
	venta = models.ForeignKey(Venta)
	descuento = models.ForeignKey(Descuento)
	def __unicode__(self):
		return '['+str(self.cantidad)+'] '+self.producto.producto.nombre
	def total(self):
		total = self.cantidad * self.producto.producto.precio
		return total

class VentaDetailForm(ModelForm):
	class Meta:
		model = VentaDetail
		exclude = ('venta',)