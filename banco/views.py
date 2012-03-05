from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from banco.models import Movimiento, MovimientoForm
from django.template import RequestContext

def read(request):
	latest_list = Movimiento.objects.order_by('id')
	total = 0
	for movimiento in latest_list:
		if movimiento.clasificacion == '2':
			total += movimiento.cantidad
		else:
			total -= movimiento.cantidad
	return render_to_response('banco/index.html',{'latest_list':latest_list, 'total':total}, context_instance = RequestContext(request))

def update(request, id = None):
	instance = None
	if id is not None:
		instance = Movimiento.objects.get(id = id)
	if request.method == 'POST':
		form = MovimientoForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/banco')
	else:
		form = MovimientoForm(instance = instance)
	return render_to_response('common/detail.html',{'form':form}, context_instance = RequestContext(request))