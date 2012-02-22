from django.conf.urls.defaults import *
from django.views.generic import ListView
from usuarios.models import Usuario

urlpatterns = patterns('',
	url(r'^create/$', 'usuarios.views.update'), #create
	url(r'^$',
        ListView.as_view(
            queryset = Usuario.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'usuarios/index.html')), #read
	url(r'^update/$', 'usuarios.views.update'), #update
	url(r'^update/(?P<id>\d+)/$', 'usuarios.views.update'), #update
)