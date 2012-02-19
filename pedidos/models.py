from django.db import models
from django.forms import ModelForm
from proveedores.models import Proveedor, Producto

completado_choices = (
	('No', 'No'),
	('Si', 'Si'),
)

class Pedido(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	proveedor  = models.ForeignKey(Proveedor)
	def total(self):
		pedidodetails = PedidoDetail.objects.filter(pedido__id = self.id)
		total = 0
		for pedidodetail in pedidodetails:
			total += pedidodetail.cantidad * pedidodetail.producto.precio
		return total
	def anticipo(self):
		anticipos = Anticipo.objects.filter(pedido__id = self.id)
		total = 0
		for anticipo in anticipos:
			total += anticipo.cantidad
		return total
	def restante(self):
		total = self.total() - self.anticipo()
		return total


class PedidoForm(ModelForm):
	class Meta:
		model = Pedido

class PedidoDetail(models.Model):
	pedido = models.ForeignKey(Pedido)
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits = 3, decimal_places = 0)
	completado = models.CharField(max_length = 2, choices = completado_choices)
	def total(self):
		total = self.producto.precio * self.cantidad
		return total

class PedidoDetailForm(ModelForm):
	def __init__(self, id_proveedor = None, *args, **kwargs):
		super (PedidoDetailForm,self ).__init__(*args,**kwargs)
		self.fields['producto'].queryset = Producto.objects.filter(proveedor__id = id_proveedor)
    
	class Meta:
		model = PedidoDetail
		exclude = ('pedido',)

class Anticipo(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	pedido = models.ForeignKey(Pedido)
	cantidad = models.DecimalField(max_digits = 9, decimal_places = 2)

class AnticipoForm(ModelForm):
	class Meta:
		model = Anticipo
		exclude = ('pedido')