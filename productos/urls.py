from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from productos.models import Producto

urlpatterns = patterns('',
    url(r'^create/$', 'productos.views.update'), #create
    url(r'^$',
        ListView.as_view(
            queryset = Producto.objects.order_by('nombre'),
            context_object_name = 'latest_list', 
            template_name = 'store/common/index.html')), #read
    url(r'^(?P<id>\d+)/$', 'productos.views.update'), #update
)