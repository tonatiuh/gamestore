from django.db import models
from django.forms import ModelForm

class Descuento(models.Model):
	nombre = models.CharField(max_length = 25)
	porcentaje = models.IntegerField()
	def __unicode__(self):
		return self.nombre

class DescuentoForm(ModelForm):
	class Meta:
		model = Descuento
