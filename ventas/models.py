from almacen.models import Almacenado
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
			total += ventadetail.total()
		return total
	def test():
		return 2

class VentaForm(ModelForm):
	class Meta:
		model = Venta

class VentaDetail(models.Model):
	id = models.AutoField(primary_key=True)
	almacenado = models.ForeignKey(Almacenado)
	venta = models.ForeignKey(Venta)
	descuento = models.ForeignKey(Descuento, blank=True, null=True)
	def __unicode__(self):
		return '['+str(self.cantidad)+'] '+self.almacenado.producto.nombre
	def total(self):
		total = self.almacenado.producto.precio
		if self.descuento:
			descuento = (self.descuento.porcentaje*total)/100
			total -= descuento
		return total

class VentaDetailForm(ModelForm):
	class Meta:
		model = VentaDetail
		exclude = ('venta',)
	def __init__(self, id_producto, *args, **kwargs):
		super (VentaDetailForm,self ).__init__(*args,**kwargs)
		self.fields['almacenado'].queryset = Almacenado.objects.filter(producto__id = id_producto)