from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from proveedores.models import Proveedor, ProveedorForm, Producto, ProductoForm

def update(request, id = None):
	instance = None
	latest_list = Producto.objects.filter(proveedor__id__exact = id)
	if id is not None:
		instance = Proveedor.objects.get(id = id)
	if request.method == 'POST':
		form = ProveedorForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/proveedores')
	else:
		form = ProveedorForm(instance = instance)
	return render_to_response('proveedores/detail.html',{'form':form, 'latest_list':latest_list})

def producto_update(request, id_proveedor = None, id = None):
	instance = None
	proveedor = Proveedor.objects.get(id = id_proveedor)
	instance = Producto(proveedor = proveedor)
	if id is not None:
		instance = Producto.objects.get(id = id)
	if request.method == 'POST':
		form = ProductoForm(request.POST, instance = instance)
		if form.is_valid():
			form = form.save()
			return HttpResponseRedirect('/proveedores/update/'+id_proveedor)
	else:
		form = ProductoForm(instance = instance)
	return render_to_response('common/detail.html',{'form':form})