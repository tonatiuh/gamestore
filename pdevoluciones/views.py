from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from pedidos.models import Pedido
from pdevoluciones.models import PDevolucion, PDevolucionForm

def update(request, id_pedido = None, id = None):
	instance = None
	if id is not None:
		instance = PDevolucion.objects.get(id = id)
		id_pedido = instance.pedidodetail.pedido.id
	if request.method == 'POST':
		form = PDevolucionForm(id_pedido, request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/pdevoluciones')
	else:
		form = PDevolucionForm(id_pedido, instance = instance)
	return render_to_response('common/detail.html',{'form':form})
