from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from descuentos.models import Descuento, DescuentoForm

def update(request, id = None):
	instance = None
	if id is not None:
		instance = Descuento.objects.get(id = id)
	if request.method == 'POST':
		form = DescuentoForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/descuentos')
	else:
		form = DescuentoForm(instance = instance)
	return render_to_response('common/detail.html',{'form':form})
