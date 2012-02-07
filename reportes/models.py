from django.db import models
from django.forms import ModelForm
from ventas.models import Venta

class Reporte(models.Model):
	fecha_start = models.DateTimeField(auto_now_add = True)
	fecha_end = models.DateTimeField(blank = True, null = True)
	saldo_inicial = models.DecimalField(max_digits = 7, decimal_places = 2, null = True, blank = True, default = 0)
	def __unicode__(self):
		return '['+str(self.fecha_start)+']'
	def total(self):
		reportedetails = ReporteDetail.objects.filter(reporte__id__exact = self.id)
		total = self.saldo_inicial
		for reportedetail in reportedetails:
			total += reportedetail.venta.total()
		retiros = Retiro.objects.filter(reporte__id__exact = self.id)
		for retiro in retiros:
			total -= retiro.cantidad
		ingresos = Ingreso.objects.filter(reporte__id__exact = self.id)
		for ingreso in ingresos:
			total += ingreso.cantidad
		return total

class ReporteDetail(models.Model):
	reporte = models.ForeignKey(Reporte)
	venta = models.ForeignKey(Venta)
	def __unicode__(self):
		return str(self.id)

class Retiro(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	reporte = models.ForeignKey(Reporte)
	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)

class RetiroForm(ModelForm):
	class Meta:
		model = Retiro
		exclude = ('reporte')

class Ingreso(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	reporte = models.ForeignKey(Reporte)
	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)

class IngresoForm(ModelForm):
	class Meta:
		model = Ingreso
		exclude = ('reporte')
