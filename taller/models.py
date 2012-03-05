from django.db import models
from clientes.models import Cliente
from django.forms import ModelForm

estatus_choices = (
	('0', 'Imposible'),
	('1', 'En revision'), 
	('2', 'Reparado'),
	('3', 'Entregado'),
)

class Reparacion(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	cliente = models.ForeignKey(Cliente)
	equipo = models.CharField(max_length = 25)
	serial = models.CharField(max_length = 25)
	problema = models.CharField(max_length = 1000)
	observacion = models.CharField(max_length = 1000)
	estatus = models.CharField(max_length = 12, choices = estatus_choices)

class ReparacionForm(ModelForm):
	class Meta:
		model = Reparacion