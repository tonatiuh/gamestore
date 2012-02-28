from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from clientes.models import Cliente

urlpatterns = patterns('',
	url(r'^create/$', 'clientes.views.update'), #create
    url(r'^$',
        ListView.as_view(
            queryset = Cliente.objects.order_by('nombre'),
            context_object_name = 'latest_list', 
            template_name = 'clientes/index.html')), #read
    url(r'^update/(?P<id>\d+)/$', 'clientes.views.update'), #update
)