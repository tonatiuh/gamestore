from django.forms import ModelForm
from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length = 150)
	primer_apellido =  models.CharField(max_length = 150)
	segundo_apellido = models.CharField(max_length = 150)
	telefono = models.CharField(max_length = 10)
	def __unicode__(self):
		return self.nombre

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente