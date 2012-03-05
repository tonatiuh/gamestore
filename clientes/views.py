from clientes.models import Cliente, ClienteForm
from historiador.models import Registro
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

def update(request, id = None):
	instance = None
	if id is not None:
		instance = Cliente.objects.get(id = id)
	#when POST
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			if id is not None:
				registro = Registro(seccion = 'clientes', accion = 'actualizo', usuario = int(request.session['user_id']))
			else:
				registro = Registro(seccion = 'clientes', accion = 'creo', usuario = int(request.session['user_id']))
			registro.save()
		return HttpResponseRedirect('/clientes/')
	#when NOT POST
	else:
		form = ClienteForm(instance = instance)
	return render_to_response('clientes/detail.html',{'form':form}, context_instance = RequestContext(request))