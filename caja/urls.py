from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from clientes.models import Cliente

urlpatterns = patterns('',
    url(r'^$', 'caja.views.index'), #index
    url(r'^cerrar$', 'caja.views.cerrar'), #cerrar
    url(r'^abrir$', 'caja.views.cerrar'), #abrir
)