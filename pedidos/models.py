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

class PedidoForm(ModelForm):
	class Meta:
		model = Pedido

class PedidoDetail(models.Model):
	pedido = models.ForeignKey(Pedido)
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits = 3, decimal_places = 0)
	completado = models.CharField(max_length = 2, choices = completado_choices)

class PedidoDetailForm(ModelForm):
	def __init__(self, id_proveedor, *args, **kwargs):
		super (PedidoDetailForm,self ).__init__(*args,**kwargs)
		self.fields['producto'].queryset = Producto.objects.filter(proveedor__id = id_proveedor)
    
	class Meta:
		model = PedidoDetail
		exclude = ('pedido',)