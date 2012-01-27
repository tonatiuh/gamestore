from django.conf.urls.defaults import *
from django.views.generic import ListView
from ventas.models import Venta

urlpatterns = patterns('',
    url(r'^create/$', 'ventas.views.create'), #create
    url(r'^$',
        ListView.as_view(
            queryset = Venta.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'store/ventas/index.html')), #read
    url(r'^update/(?P<id_venta>\d+)/$', 'ventas.views.update'), #update

	url(r'^update/(?P<id_venta>\d+)/details/create$', 'ventas.views.details_create'), #create
	url(r'^update/(?P<id_venta>\d+)/details/update/(?P<id_ventadetail>\d+)$', 'ventas.views.details_update'), #update
)