from clientes.models import Cliente, ClienteForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def update(request, id_cliente = None):
	instance = None
	if id_cliente is not None:
		instance = Cliente.objects.get(id = id_cliente)
	#when POST
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/clientes/')
	#when NOT POST
	else:
		form = ClienteForm(instance = instance)
	return render_to_response('clientes/detail.html',{'form':form})