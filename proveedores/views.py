from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from proveedores.models import Proveedor, ProveedorForm

def update(request, id = None):
	instance = None
	if id is not None:
		instance = Proveedor.objects.get(id = id)
	if request.method == 'POST':
		form = ProveedorForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/proveedores')
	else:
		form = ProveedorForm(instance = instance)
	return render_to_response('common/detail.html',{'form':form})
