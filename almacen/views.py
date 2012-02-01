from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from almacen.models import AlmacenDetail, AlmacenDetailForm

def create(request):
	#when POST
	if request.method == 'POST':
		form = AlmacenDetailForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/almacen/')
	else:
		form = AlmacenDetailForm()
	return render_to_response('almacen/detail.html', {'form':form}, context_instance=RequestContext(request))

def update(request, almacendetail_id):
	almacendetail = AlmacenDetail.objects.get(id = almacendetail_id)
	#when POST
	if request.method == 'POST':
		form = AlmacenDetailForm(request.POST, instance = almacendetail)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/almacen/')
	#when NOT POST
	else:
		form = AlmacenDetailForm(instance = almacendetail)
	return render_to_response('almacen/detail.html',{'form':form})