from django.conf.urls.defaults import *
from django.views.generic import ListView
from banco.models import Movimiento

urlpatterns = patterns('',
	url(r'^create/$', 'banco.views.update'), #create
	url(r'^$', 'banco.views.read'), #read
	url(r'^update/(?P<id>\d+)/$', 'banco.views.update'), #update
)