from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from almacen.models import AlmacenDetail

urlpatterns = patterns('',
	url(r'^create/$', 'almacen.views.create'), #create
    url(r'^$',
        ListView.as_view(
            queryset = AlmacenDetail.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'almacen/index.html')), #read
    url(r'^update/(?P<almacendetail_id>\d+)/$', 'almacen.views.update'), #update
)