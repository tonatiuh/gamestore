from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from apartado.models import ApartadoDetail, ApartadoDetailForm
from almacen.models import Producto
from django.template import RequestContext

def create(request):
	#when POST
	if request.method == 'POST':
		form = ApartadoDetailForm(request.POST)
		if form.is_valid():
			apartadodetail = form.save(commit = False)
			if (apartadodetail.cantidad < apartadodetail.producto.cantidad):
				form.save()
			else:
				return HttpResponse('No hay unidades suficientes disponibles en el almacen')
		return HttpResponseRedirect('/apartado/')
	#when NOT POST
	else:
		form = ApartadoDetailForm()
	return render_to_response('apartado/detail.html', {'form':form}, context_instance=RequestContext(request))

def update(request, id_apartadodetail):
	#when POST
	if request.method == 'POST':
		form = ApartadoDetailForm(request.POST)
		if form.is_valid():
			apartadodetail = form.save(commit = False)
			if (apartadodetail.cantidad < apartadodetail.producto.cantidad):
				form.save()
			else:
				return HttpResponse('No hay unidades suficientes disponibles en el almacen')
		return HttpResponseRedirect('/apartado/')
	#when NOT POST
	else:
		apartadodetail = ApartadoDetail.objects.get(id = id_apartadodetail)
		form = ApartadoDetailForm(instance = apartadodetail)
	return render_to_response('apartado/detail.html', {'form':form}, context_instance=RequestContext(request))