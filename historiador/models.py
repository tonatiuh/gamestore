from django.db import models
from usuarios.models import Usuario

class Registro(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	seccion = models.CharField(max_length = 25)
	accion = models.CharField(max_length = 25)
	usuario = models.IntegerField()
	def real_usuario(self):
		usuario = Usuario.objects.get(id = self.usuario)
		return usuario