from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from almacen.models import Almacenado, AlmacenadoForm
from django.views.generic.list_detail import object_list

def create(request):
	#when POST
	if request.method == 'POST':
		form = AlmacenadoForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/almacen/')
	else:
		form = AlmacenadoForm()
	return render_to_response('almacen/detail.html', {'form':form}, context_instance=RequestContext(request))

def update(request, id, id_producto = None):
	instance = None
	if id is not None:
		instance = Almacenado.objects.get(id = id)
	if request.method == 'POST':
		form = AlmacenadoForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/almacen')
	else:
		form = AlmacenadoForm(instance = instance)
	return render_to_response('common/detail.html',{'form':form}, context_instance = RequestContext(request))

def productos_read(request, id):
	queryset = Almacenado.objects.filter(producto__id = id)
	return object_list(request, queryset = queryset, template_name = 'almacen/productos_read.html')