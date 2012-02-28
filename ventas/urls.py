from django.conf.urls.defaults import *
from django.views.generic import ListView
from ventas.models import Venta

urlpatterns = patterns('',
    url(r'^create/$', 'ventas.views.update'), #create
    url(r'^$',
        ListView.as_view(
            queryset = Venta.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'ventas/index.html')), #read
    url(r'^update/(?P<id>\d+)/$', 'ventas.views.update'), #update

	url(r'^update/(?P<id_venta>\d+)/productos$', 'ventas.views.productos_read'), #create - select product type
	url(r'^update/(?P<id_venta>\d+)/productos/read/(?P<id_producto>\d+)/details/create$', 'ventas.views.details_update'), #create
	url(r'^update/(?P<id_venta>\d+)/productos/read/(?P<id_producto>\d+)/details/update/(?P<id>\d+)$', 'ventas.views.details_update'), #update
)