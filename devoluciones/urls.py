from django.conf.urls.defaults import *
from django.views.generic import ListView
from devoluciones.models import Devolucion
from ventas.models import Venta

urlpatterns = patterns('',
	url(r'^create$',
        ListView.as_view(
            queryset = Venta.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'store/devoluciones/create.html')), #shows -ventas
    url(r'^create/ventas/(?P<id_venta>\d+)/$', 'devoluciones.views.ventas_read'), #shows -ventasdetails
    url(r'^create/ventas/(?P<id_venta>\d+)/details/(?P<id_ventadetail>\d+)/$', 'devoluciones.views.create'), #create
	url(r'^$', 'devoluciones.views.read'), #read
	url(r'^update/(?P<id_devolucion>\d+)/$', 'devoluciones.views.update'), #update
)