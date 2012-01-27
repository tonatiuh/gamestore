from ventas.models import Venta, VentaDetail
from django.forms import ModelForm
from django.db import models

class Devolucion(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	venta = models.ForeignKey(Venta)
	ventadetail = models.ForeignKey(VentaDetail)
	cantidad = models.DecimalField(max_digits = 2, decimal_places = 0)
	motivo = models.TextField()
	def __unicode__(self):
		return '['+str(self.cantidad)+']['+str(self.ventadetail.cantidad)+'] '+str(self.ventadetail.producto.nombre)+' ['+(self.venta.cliente.nombre)+' '+(self.venta.cliente.primer_apellido)+']'

class DevolucionForm(ModelForm):
	class Meta:
		model = Devolucion
		exclude = ( 'venta', 'ventadetail',)