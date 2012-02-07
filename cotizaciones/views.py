from cotizaciones.models import Cotizacion, CotizacionForm, CotizacionDetail, CotizacionDetailForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse

def create(request):
	#when POST
	if request.method == 'POST':
		form = CotizacionForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/cotizaciones/')
	else:
		form = CotizacionForm()
	return render_to_response('cotizaciones/detail.html', {'form':form}, context_instance=RequestContext(request))

def update(request, id_cotizacion = None):
	cotizacion = None
	latest_list = False
	if id_cotizacion is not None:
		cotizacion = Cotizacion.objects.get(id = id_cotizacion)
		latest_list = CotizacionDetail.objects.filter(cotizacion = id_cotizacion)
	#when POST
	if request.method == 'POST':
		form = CotizacionForm(request.POST, instance = cotizacion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/cotizaciones/')
	#when NOT POST
	else:
		form = CotizacionForm(instance = cotizacion)
	return render_to_response('cotizaciones/detail.html',{'form':form, 'cotizacion':cotizacion, 'latest_list': latest_list}, context_instance=RequestContext(request))

def details_create(request, id_cotizacion):
	#when POST
	if request.method == 'POST':
		cotizacion = Cotizacion.objects.get(id = id_cotizacion)
		cotizaciondetail = CotizacionDetail(cotizacion = cotizacion)
		form = CotizacionDetailForm(request.POST, instance = cotizaciondetail)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/cotizaciones/update/'+id_cotizacion)
		else:
			return HttpResponse('no fue posible hacer la operacion')
	#when NOT POST
	else:
		form = CotizacionDetailForm()
	return render_to_response('common/detail.html', {'form':form}, context_instance=RequestContext(request))

def details_update(request, id_cotizacion, id_cotizaciondetail):
	#when POST
	if request.method == 'POST':
		cotizacion = Cotizacion.objects.get(id = id_cotizacion)
		cotizaciondetail = CotizacionDetail.objects.get(id = id_cotizaciondetail)
		cotizaciondetail.cotizacion = cotizacion
		form = CotizacionDetailForm(request.POST, instance = cotizaciondetail)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/cotizaciones/update/'+id_cotizacion)
	#when NOT POST
	else:
		cotizaciondetail = CotizacionDetail.objects.get(id = id_cotizaciondetail)
		form = CotizacionDetailForm(instance = cotizaciondetail)
	return render_to_response('common/detail.html', {'form':form}, context_instance=RequestContext(request))

def update_printit(request, id_cotizacion = None):
	cotizacion = None
	latest_list = False
	if id_cotizacion is not None:
		cotizacion = Cotizacion.objects.get(id = id_cotizacion)
		latest_list = CotizacionDetail.objects.filter(cotizacion = id_cotizacion)
	#when POST
	if request.method == 'POST':
		form = CotizacionForm(request.POST, instance = cotizacion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/cotizaciones/')
	#when NOT POST
	else:
		form = CotizacionForm(instance = cotizacion)
	return render_to_response('cotizaciones/printit.html',{'form':form, 'cotizacion':cotizacion, 'latest_list': latest_list}, context_instance=RequestContext(request))