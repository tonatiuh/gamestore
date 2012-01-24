from ventas.models import Venta, VentaForm, Venta_description
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def detail(request, id = None):
	instance = None
	latest_list = False
	if id is not None:
		instance = Venta.objects.get(id = id)
		latest_list = Venta_description.objects.filter(venta = id)
	#when POST
	if request.method == 'POST':
		form = VentaForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/ventas/')
	#when NOT POST
	else:
		form = VentaForm(instance = instance)
	return render_to_response('store/ventas/detail.html',{'form':form, 'latest_list':latest_list})