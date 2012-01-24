from clientes.models import Cliente, ClienteForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def detail(request, id = None):
	instance = None
	if id is not None:
		instance = Producto.objects.get(id = id)
	#when POST
	if request.method == 'POST':
		form = ProductoForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/clientes/')
	#when NOT POST
	else:
		form = ProductoForm(instance = instance)
	return render_to_response('store/common/detail.html',{'form':form})