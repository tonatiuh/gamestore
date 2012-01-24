from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from store.models import Cliente, ClienteForm
from django.http import  HttpResponseRedirect, HttpResponse

def cliente_detail(request, id = None):
	instance = None
	if id is not None:
		instance = Cliente.objects.get(id = id)
	#when POST
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/clientes/')
	#when NOT POST
	else:
		form = ClienteForm(instance = instance)
	return render_to_response('store/common/detail.html',{'form':form})

"""
def producto_detail(request, id = None):
	instance = None
	if id is not None:
		instance = Producto.objects.get(id = id)
	#when POST
	if request.method == 'POST':
		form = ProductoForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/productos/')
	#when NOT POST
	else:
		form = ProductoForm(instance = instance)
	return render_to_response('store/common/detail.html',{'form':form})

def venta_detail(request, id = None):
	instance = None
	if id is not None:
		instance = Venta.objects.get(id = id)
	#when POST
	if request.method == 'POST':
		form = VentaForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/ventas/')
	#when NOT POST
	else:
		form = VentaForm(instance = instance)
	return render_to_response('store/common/detail.html',{'form':form})
"""