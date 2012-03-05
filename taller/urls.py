from django.conf.urls.defaults import *
from django.views.generic import ListView
from taller.models import Reparacion

urlpatterns = patterns('',
	url(r'^create/$', 'taller.views.create'), #create
	url(r'^$',
        ListView.as_view(
            queryset = Reparacion.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'taller/index.html')), #read
	url(r'^update/(?P<id>\d+)/$', 'taller.views.update'), #update
	url(r'^update/(?P<id>\d+)/delete$', 'taller.views.delete'), #delete
)