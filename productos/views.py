from productos.models import Producto, ProductoForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

def update(request, id = None):
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
	return render_to_response('common/detail.html',{'form':form}, context_instance = RequestContext(request))