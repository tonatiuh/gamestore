from reportes.models import Reporte, ReporteDetail
from django.shortcuts import render_to_response
from django.http import HttpResponse

def read(self, reporte_id):
	reporte = Reporte.objects.get(id = reporte_id)
	reportedetails = ReporteDetail.objects.filter(reporte__id__exact = reporte_id)
	return render_to_response('reportes/read.html', {'latest_list': reportedetails, 'reporte':reporte})