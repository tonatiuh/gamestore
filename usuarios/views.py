from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from usuarios.models import Usuario, UsuarioForm

def update(request, id = None):
	instance = None
	if id is not None:
		instance = Usuario.objects.get(id = id)
	if request.method == 'POST':
		form = UsuarioForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/usuarios')
	else:
		form = UsuarioForm(instance = instance)
	return render_to_response('common/detail.html',{'form':form})