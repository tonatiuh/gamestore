from ventas.models import Venta, VentaDetail
from devoluciones.models import Devolucion, DevolucionForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

#	latest_list = VentaDetail.objects.filter(venta__id__exact = 1)

def ventas_read(request, id_venta):
	latest_list = VentaDetail.objects.filter(venta = id_venta)
	return render_to_response('store/devoluciones/detail.html',{'latest_list':latest_list}, context_instance=RequestContext(request))

def create(request, id_venta, id_ventadetail):
	#when POST
	if request.method == 'POST':
		venta = Venta.objects.get(id = id_venta)
		ventadetail = VentaDetail.objects.get(id = id_ventadetail)
		devolucion = Devolucion(venta = venta, ventadetail = ventadetail)
		form = DevolucionForm(request.POST, instance = devolucion)
		if form.is_valid():
			ventadetail.cantidad -= devolucion.cantidad
			ventadetail.save()
			form.save()
		return HttpResponseRedirect('/devoluciones/')
	else:
		devolucion = Devolucion.objects.filter(ventadetail__id__exact = id_ventadetail)
		if devolucion:
			return HttpResponseRedirect('/devoluciones/update/'+str(devolucion[0].id))
		else:
			form = DevolucionForm()
	return render_to_response('store/devoluciones/detail2.html', {'form':form}, context_instance=RequestContext(request))

def read(request):
	latest_list = Devolucion.objects.all
	return render_to_response('store/devoluciones/index.html',{'latest_list':latest_list}, context_instance=RequestContext(request))

def update(request, id_devolucion):
	devolucion = Devolucion.objects.get(id = id_devolucion)
	# POST
	if request.method == 'POST':
		form = DevolucionForm(request.POST, instance = devolucion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/devoluciones/')
	form = DevolucionForm(instance = devolucion)
	return render_to_response('store/common/detail.html',{'form':form})

