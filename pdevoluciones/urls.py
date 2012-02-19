from django.conf.urls.defaults import *
from django.views.generic import ListView
from pdevoluciones.models import PDevolucion
from pedidos.models import Pedido

urlpatterns = patterns('',
	url(r'^create/pedidos/(?P<id_pedido>\d+)$', 'pdevoluciones.views.update'), #create
	url(r'^$',
        ListView.as_view(
            queryset = PDevolucion.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'pdevoluciones/index.html')), #read
    url(r'^create/$',
        ListView.as_view(
            queryset = Pedido.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'pdevoluciones/pedidos.html')), #read - pedidos
	url(r'^update/(?P<id>\d+)$', 'pdevoluciones.views.update'), #create
)