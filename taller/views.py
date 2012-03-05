# Create your views here.

def update(request, id = None):
	instance = None
	if id is not None:
		instance = Reparacion.objects.get(id = id)
	if request.method == 'POST':
		form = ReparacionForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/taller')
	else:
		form = ReparacionForm(instance = instance)
	return render_to_response('common/detail.html',{'form':form})