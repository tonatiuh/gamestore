from django.conf.urls.defaults import *
from django.views.generic import ListView
from pedidos.models import Pedido, PedidoDetail

urlpatterns = patterns('',
	url(r'^create/$', 'pedidos.views.update'), #create
	url(r'^$',
        ListView.as_view(
            queryset = Pedido.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'pedidos/index.html')), #read
    url(r'^update/(?P<id>\d+)/$', 'pedidos.views.update'), #update

    url(r'^update/(?P<id_pedido>\d+)/details/create$', 'pedidos.views.detail_update'), #details/create
    url(r'^update/(?P<id_pedido>\d+)/details/update/(?P<id>\d+)$', 'pedidos.views.detail_update'), #details/update

    url(r'^update/(?P<id_pedido>\d+)/anticipos/create$', 'pedidos.views.anticipo_update'), #anticipos/create
    url(r'^update/(?P<id_pedido>\d+)/anticipos/update/(?P<id>\d+)$', 'pedidos.views.anticipo_update'), #details/update
)