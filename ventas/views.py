from ventas.models import Venta, VentaForm, VentaDetail, VentaDetailForm
from almacen.models import Almacenado
from reportes.models import Reporte, ReporteDetail
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list_detail import object_list
from django.db.models import Count

def update(request, id = None):
	instance = None
	latest_list = None
	if id is not None:
		instance = Venta.objects.get(id = id)
		latest_list = VentaDetail.objects.filter(venta__id = id)
	if request.method == 'POST':
		form = VentaForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ventas')
	else:
		form = VentaForm(instance = instance)
	return render_to_response('ventas/detail.html', {'form':form, 'latest_list':latest_list, 'venta':instance}, context_instance=RequestContext(request))

def productos_read(request, id_venta): #list all the products
	queryset = Almacenado.objects.values('producto__nombre', 'producto__id').annotate(total = Count('codigo'))
	return object_list(request, queryset = queryset, template_name = 'ventas/productos_read.html')

def details_update(request, id_venta, id_producto, id = None):
	instance = None
	if id is not None:
		instance = VentaDetail.objects.get(id = id)
	if request.method == 'POST':
		venta = Venta.objects.get(id = id_venta)
		form = VentaDetailForm(id_producto, request.POST, instance = instance)
		if form.is_valid():
			ventadetail = form.save(commit = False)
			ventadetail.venta = venta
			ventadetail.save()
			return HttpResponseRedirect('/ventas/update/'+id_venta)
	else:
		form = VentaDetailForm(id_producto, instance = instance)
	return render_to_response('common/detail.html',{'form':form}, context_instance = RequestContext(request))