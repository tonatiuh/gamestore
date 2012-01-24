from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gamestore.views.home', name='home'),
    # url(r'^gamestore/', include('gamestore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^clientes/', include('clientes.urls')),
    url(r'^productos/', include('productos.urls')),
    url(r'^ventas/', include('ventas.urls')),

    #url(r'^productos/add/$', 'store.views.producto_detail'),

)
