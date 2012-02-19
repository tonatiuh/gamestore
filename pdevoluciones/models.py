from django.db import models
from django.forms import ModelForm
from pedidos.models import PedidoDetail

class PDevolucion(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	pedidodetail = models.ForeignKey(PedidoDetail)
	cantidad = models.IntegerField()
	motivo = models.TextField()

class PDevolucionForm(ModelForm):
	class Meta:
		model = PDevolucion
	def __init__(self, id_pedido, *args, **kwargs):
		super (PDevolucionForm,self ).__init__(*args,**kwargs)
		self.fields['pedidodetail'].queryset = PedidoDetail.objects.filter(pedido__id = id_pedido)