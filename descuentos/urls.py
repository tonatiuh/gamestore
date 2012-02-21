from django.conf.urls.defaults import *
from django.views.generic import ListView
from descuentos.models import Descuento

urlpatterns = patterns('',
	url(r'^create/$', 'descuentos.views.update'), #create
	url(r'^$',
        ListView.as_view(
            queryset = Descuento.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'descuentos/index.html')), #read
    url(r'^update/(?P<id>\d+)/$', 'descuentos.views.update'), #update
)