from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from clientes.models import Cliente

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset = Cliente.objects.order_by('nombre'),
            context_object_name = 'latest_list', 
            template_name = 'store/common/index.html')),
    url(r'^(?P<id>\d+)/$', 'clientes.views.detail'),
    url(r'^add/$', 'clientes.views.detail'),
)