from django.conf.urls.defaults import *
from django.views.generic import ListView

urlpatterns = patterns('',
	url(r'^salir/$', 'guardian.views.logout'), #logout
)