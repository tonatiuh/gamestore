from ventas.models import Venta, VentaForm, VentaDetail, VentaDetailForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def create(request):
	#when POST
	if request.method == 'POST':
		form = VentaForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/ventas/')
	else:
		form = VentaForm()
	return render_to_response('store/ventas/detail.html', {'form':form}, context_instance=RequestContext(request))

def update(request, id_venta = None):
	venta = None
	latest_list = False
	if id_venta is not None:
		venta = Venta.objects.get(id = id_venta)
		latest_list = VentaDetail.objects.filter(venta = id_venta)
	#when POST
	if request.method == 'POST':
		form = VentaForm(request.POST, instance = venta)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/ventas/')
	#when NOT POST
	else:
		form = VentaForm(instance = venta)
	return render_to_response('store/ventas/detail.html',{'form':form, 'latest_list':latest_list}, context_instance=RequestContext(request))

def details_create(request, id_venta):
	#when POST
	if request.method == 'POST':
		venta = Venta.objects.get(id = id_venta)
		ventadetail = VentaDetail(venta = venta)
		form = VentaDetailForm(request.POST, instance = ventadetail)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/ventas/update/'+id_venta)
	#when NOT POST
	else:
		form = VentaDetailForm()
	return render_to_response('store/common/detail.html', {'form':form}, context_instance=RequestContext(request))

def details_update(request, id_venta, id_ventadetail):
	#when POST
	if request.method == 'POST':
		venta = Venta.objects.get(id = id_venta)
		ventadetail = VentaDetail.objects.get(id = id_ventadetail)
		ventadetail.venta = venta
		form = VentaDetailForm(request.POST, instance = ventadetail)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/ventas/update/'+id_venta)
	#when NOT POST
	else:
		ventadetail = VentaDetail.objects.get(id = id_ventadetail)
		form = VentaDetailForm(instance = ventadetail)
	return render_to_response('store/common/detail.html', {'form':form}, context_instance=RequestContext(request))