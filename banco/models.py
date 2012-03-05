from django.db import models
from django.forms import ModelForm

movimiento_choices = (
	('1', 'retiro'),
	('2', 'deposito'),
)

class Movimiento(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	clasificacion = models.CharField(max_length = 20, choices = movimiento_choices)
	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
	razon = models.TextField()

class MovimientoForm(ModelForm):
	class Meta:
		model = Movimiento