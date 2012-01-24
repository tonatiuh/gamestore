from ventas.models import Venta, VentaForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def detail(request, id = None):
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
	return render_to_response('store/ventas/detail.html',{'form':form})