from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from ventas.models import Venta

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset = Venta.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'store/ventas/index.html')),
    url(r'^(?P<id>\d+)/$', 'ventas.views.detail'),
    url(r'^add/$', 'ventas.views.detail'),
)