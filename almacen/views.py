from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from almacen.models import Producto, ProductoForm

def create(request):
	#when POST
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/almacen/')
	else:
		form = ProductoForm()
	return render_to_response('almacen/detail.html', {'form':form}, context_instance=RequestContext(request))

def update(request, almacendetail_id):
	producto = Producto.objects.get(id = almacendetail_id)
	#when POST
	if request.method == 'POST':
		form = ProductoForm(request.POST, instance = producto)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/almacen/')
	#when NOT POST
	else:
		form = ProductoForm(instance = producto)
	return render_to_response('almacen/detail.html',{'form':form})