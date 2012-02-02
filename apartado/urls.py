from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from apartado.models import ApartadoDetail

urlpatterns = patterns('',
	url(r'^create/$', 'apartado.views.create'), #create
    url(r'^$',
        ListView.as_view(
            queryset = ApartadoDetail.objects.order_by('-id'),
            context_object_name = 'latest_list', 
            template_name = 'apartado/index.html')), #read
    url(r'^update/(?P<id_apartadodetail>\d+)/$', 'apartado.views.update'), #update
)