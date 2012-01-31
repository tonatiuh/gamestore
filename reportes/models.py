from django.db import models
from ventas.models import Venta

class Reporte(models.Model):
	fecha_start = models.DateTimeField(auto_now_add = True)
	fecha_end = models.DateTimeField(blank = True, null = True)
	def __unicode__(self):
		return '['+str(self.fecha_start)+']'
	def total(self):
		reportedetails = ReporteDetail.objects.filter(reporte__id__exact = self.id)
		total = 0
		for reportedetail in reportedetails:
			total += reportedetail.venta.total()
		return total

class ReporteDetail(models.Model):
	reporte = models.ForeignKey(Reporte)
	venta = models.ForeignKey(Venta)
	def __unicode__(self):
		return str(self.id)
