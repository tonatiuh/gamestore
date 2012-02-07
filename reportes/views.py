from reportes.models import Reporte, ReporteDetail, Retiro, RetiroForm, Ingreso, IngresoForm
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def read(self, reporte_id):
	reporte = Reporte.objects.get(id = reporte_id)
	reportedetails = ReporteDetail.objects.filter(reporte__id__exact = reporte_id)
	retiros = Retiro.objects.filter(reporte__id__exact = reporte_id)
	ingresos = Ingreso.objects.filter(reporte__id__exact = reporte_id)
	return render_to_response('reportes/read.html', {'reportedetails': reportedetails, 'retiros': retiros, 'ingresos': ingresos, 'reporte':reporte})

def retiro(request):
	reporte = Reporte.objects.latest('id')
	if (reporte.fecha_end == None):
		# POST
		if request.method == 'POST':
			form = RetiroForm(request.POST)
			if form.is_valid():
				retiro = form.save(commit = False)
				retiro.reporte = reporte
				if (reporte.total > retiro.cantidad):
					retiro.save()
				else:
					return HttpResponse('No hay suficientes fondos')
			return HttpResponseRedirect('/reportes/')
		form = RetiroForm()
	return render_to_response('common/detail.html',{'form':form})

def ingreso(request):
	reporte = Reporte.objects.latest('id')
	if (reporte.fecha_end == None):
		# POST
		if request.method == 'POST':
			form = IngresoForm(request.POST)
			if form.is_valid():
				ingreso = form.save(commit = False)
				ingreso.reporte = reporte
				ingreso.save()
			return HttpResponseRedirect('/reportes/')
		form = IngresoForm()
	return render_to_response('common/detail.html',{'form':form})