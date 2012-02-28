from django.conf.urls.defaults import *
from django.views.generic import ListView
from historiador.models import Registro
	
urlpatterns = patterns('',
	url(r'^$',
        ListView.as_view(
            queryset = Registro.objects.order_by('id'),
            context_object_name = 'latest_list', 
            template_name = 'historiador/index.html')), #read
)