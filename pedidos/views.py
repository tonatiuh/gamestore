from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from pedidos.models import Pedido, PedidoForm, PedidoDetail, PedidoDetailForm

def update(request, id = None):
	instance = None
	if id is not None:
		instance = Pedido.objects.get(id = id)
	if request.method == 'POST':
		form = PedidoForm(request.POST, instance = instance)
		if form.is_valid():
			f = form.save()
			return HttpResponseRedirect('/pedidos/update/'+str(f.id))
	else:
		form = PedidoForm(instance = instance)
	latest_list = PedidoDetail.objects.filter(pedido__id__exact = id)
	return render_to_response('pedidos/detail.html',{'form':form, 'latest_list':latest_list})

def detail_update(request, id_pedido, id = None):
	instance = None
	pedido = Pedido.objects.get(id = id_pedido)
	instance = PedidoDetail(pedido = pedido)
	if id is not None:
		instance = PedidoDetail.objects.get(id = id)
	if request.method == 'POST':
		form = PedidoDetailForm(pedido.proveedor.id, request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/pedidos/update/'+str(id_pedido))
	else:
		form = PedidoDetailForm(pedido.proveedor.id, instance = instance)
	return render_to_response('common/detail.html',{'form':form})