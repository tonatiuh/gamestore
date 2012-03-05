from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from pedidos.models import Pedido, PedidoForm, PedidoDetail, PedidoDetailForm, Anticipo, AnticipoForm
from django.template import RequestContext

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
	pedidos = PedidoDetail.objects.filter(pedido__id__exact = id)
	anticipos = Anticipo.objects.filter(pedido__id__exact = id)
	return render_to_response('pedidos/detail.html',{'form':form, 'pedidos':pedidos, 'pedido':instance, 'anticipos':anticipos}, context_instance = RequestContext(request))

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
	return render_to_response('common/detail.html',{'form':form}, context_instance = RequestContext(request))

def anticipo_update(request, id_pedido = None, id = None):
	instance = None
	pedido = Pedido.objects.get(id = id_pedido)
	instance = Anticipo(pedido = pedido)
	if id is not None:
		instance = Anticipo.objects.get(id = id)
	if request.method == 'POST':
		form = AnticipoForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/pedidos/update/'+str(id_pedido))
	else:
		form = AnticipoForm(instance = instance)
	return render_to_response('common/detail.html',{'form':form})