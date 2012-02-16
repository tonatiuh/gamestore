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

	url(r'^update/(?P<id_proveedor>\d+)/productos/create$', 'proveedores.views.producto_update'), #update
	url(r'^update/(?P<id_proveedor>\d+)/productos/update/(?P<id>\d+)$', 'proveedores.views.producto_update'), #update
)