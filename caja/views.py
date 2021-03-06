from django.shortcuts import render_to_response
from reportes.models import Reporte, ReporteDetail
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import datetime

def index(request):
	reporte = Reporte.objects.latest('id')
	if (reporte.fecha_end == None):
		reportedetails = ReporteDetail.objects.filter(reporte__id__exact = reporte.id)
		return render_to_response('caja/index.html', {'latest_list': reportedetails, 'reporte': reporte}, context_instance=RequestContext(request))
	else:
		return render_to_response('caja/index.html', {}, context_instance = RequestContext(request))

def abrir(request):
	reporte = Reporte(fecha_start = datetime.datetime.now())
	reporte.save()
	return HttpResponseRedirect('/caja')


def cerrar(request):
	reporte = Reporte.objects.latest('id')
	reporte.fecha_end = datetime.datetime.now()
	reporte.save()
	return HttpResponseRedirect('/caja')