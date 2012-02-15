from django.conf.urls.defaults import *
from django.views.generic import ListView
from proveedores.models import Proveedor

urlpatterns = patterns('',
	url(r'^create/$', 'proveedores.views.update'), #create
	url(r'^$',
        ListView.as_view(
            queryset = Proveedor.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'proveedores/index.html')), #read
	url(r'^update/(?P<id>\d+)/$', 'proveedores.views.update'), #update
)