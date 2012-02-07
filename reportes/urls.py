from django.conf.urls.defaults import *
from django.views.generic import ListView
from reportes.models import Reporte

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset = Reporte.objects.order_by('-id'),
            context_object_name = 'latest_list', 
            template_name = 'reportes/index.html')), #read
    url(r'^read/(?P<reporte_id>\d+)/$', 'reportes.views.read'), #update
    url(r'^retiro$', 'reportes.views.retiro'), #retiro
    url(r'^ingreso$', 'reportes.views.ingreso'), #ingreso
)