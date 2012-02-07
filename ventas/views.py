from ventas.models import Venta, VentaForm, VentaDetail, VentaDetailForm
from almacen.models import Producto
from reportes.models import Reporte, ReporteDetail
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def create(request):
	#when POST
	if request.method == 'POST':
		form = VentaForm(request.POST)
		if form.is_valid():
			form.save()
			venta = Venta.objects.latest('id')
			reporte = Reporte.objects.latest('id')
			reportedetail = ReporteDetail(venta = venta, reporte = reporte)
			reportedetail.save()
		return HttpResponseRedirect('/ventas/')
	else:
		form = VentaForm()
	return render_to_response('ventas/detail.html', {'form':form}, context_instance=RequestContext(request))

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
	return render_to_response('ventas/detail.html',{'form':form, 'latest_list':latest_list, 'venta':venta}, context_instance=RequestContext(request))

def details_create(request, id_venta):
	#when POST
	if request.method == 'POST':
		venta = Venta.objects.get(id = id_venta)
		ventadetail = VentaDetail(venta = venta)
		form = VentaDetailForm(request.POST, instance = ventadetail)
		if form.is_valid():
			ventadetail = form.save(commit = False)
			productoalmacen = Producto.objects.filter(producto__id__exact = ventadetail.producto.id)
			if not productoalmacen:
				return HttpResponse('Este producto no esta en el almacen. Agregalo primero.')
			productoalmacen = Producto.objects.get(id = productoalmacen[0].id)
			if (ventadetail.cantidad <= productoalmacen.cantidad):
				productoalmacen.cantidad -= ventadetail.cantidad
				productoalmacen.save()
			else:
				return HttpResponse('No hay unidades suficientes en el almacen.')
			form.save()
		return HttpResponseRedirect('/ventas/update/'+id_venta)
	#when NOT POST
	else:
		form = VentaDetailForm()
	return render_to_response('common/detail.html', {'form':form}, context_instance=RequestContext(request))

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
	return render_to_response('common/detail.html', {'form':form}, context_instance=RequestContext(request))