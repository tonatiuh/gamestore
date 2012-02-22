from django.db import models
from django.forms import ModelForm
from django import forms

class Usuario(models.Model):
	nombre = models.CharField(max_length = 25)
	contrasena = models.CharField(max_length = 25)
	def __unicode__(self):
		return self.nombre

class UsuarioForm(forms.ModelForm):

	contrasena = forms.CharField(widget=forms.PasswordInput()) 

	class Meta:
		model = Usuario