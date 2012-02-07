from django.conf.urls.defaults import *
from django.views.static import *  #for media
from django.conf import settings #for media

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gamestore.views.home', name='home'),
    # url(r'^gamestore/', include('gamestore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Required to make static serving work 
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^clientes/', include('clientes.urls')),
    url(r'^productos/', include('productos.urls')),
    url(r'^ventas/', include('ventas.urls')),
    url(r'^devoluciones/', include('devoluciones.urls')),
    url(r'^caja/', include('caja.urls')),
    url(r'^reportes/', include('reportes.urls')),
    url(r'^almacen/', include('almacen.urls')),
    url(r'^apartado/', include('apartado.urls')),
    url(r'^cotizaciones/', include('cotizaciones.urls')),

    #url(r'^productos/add/$', 'store.views.producto_detail'),

)
