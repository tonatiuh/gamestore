from django.conf.urls.defaults import *
from django.views.generic import ListView
from almacen.models import Almacenado
from django.db.models import Count

urlpatterns = patterns('',
	url(r'^create/$', 'almacen.views.create'), #create
    url(r'^$',
        ListView.as_view(
            queryset = Almacenado.objects.values('producto__nombre', 'producto__id').annotate(total = Count('codigo')),
            context_object_name = 'latest_list', 
            template_name = 'almacen/index.html')), #read product groups
    url(r'^read/productos/(?P<id>\d+)/$', 'almacen.views.productos_read'), #read/productos
    url(r'^read/productos/(?P<id_producto>\d+)/update/(?P<id>\d+)/$', 'almacen.views.update'), #update
    url(r'^update/(?P<id>\d+)/$', 'almacen.views.update'), #update
)