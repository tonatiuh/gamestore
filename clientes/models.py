from django.forms import ModelForm
from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length = 150)
	primer_apellido =  models.CharField(max_length = 150)
	segundo_apellido = models.CharField(max_length = 150)
	telefono = models.CharField(max_length = 10)
	domicilio = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.nombre+' '+self.primer_apellido

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente