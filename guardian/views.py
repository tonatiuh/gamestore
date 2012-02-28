from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from usuarios.models import Usuario, UsuarioForm
from django.template import RequestContext

def login(request, id = None):
	request.session['user_id'] = None
	if request.method == 'POST':
		form = UsuarioForm(request.POST)
		request.session['user_id'] = None
		if form.is_valid():
			attempt = form.save(commit = False)
			try:
				coincident = Usuario.objects.get(nombre = attempt.nombre)
			except Exception:
				coincident = None
			if coincident:
				if (coincident.contrasena == attempt.contrasena):
					request.session['user_id'] = coincident.id
				else:
					return HttpResponse('Contrasena incorrecta')
			else:
				return HttpResponse('Usuario no registrado.')
	else:
		form = UsuarioForm()
	login_attempt = True
	return render_to_response('guardian/index.html',{'form':form, 'login_attempt':login_attempt}, context_instance = RequestContext(request))

def logout(request):
	del request.session['user_id']
	return HttpResponseRedirect('/')