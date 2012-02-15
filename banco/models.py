from django.db import models
from django.forms import ModelForm

class MovimientoClasificacion(models.Model):
	nombre = models.CharField(max_length = 20)
	def __unicode__(self):
		return self.nombre

class Movimiento(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	clasificacion = models.ForeignKey(MovimientoClasificacion)
	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
	razon = models.TextField()

class MovimientoForm(ModelForm):
	class Meta:
		model = Movimiento