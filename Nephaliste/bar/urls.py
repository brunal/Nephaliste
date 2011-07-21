from django.conf.urls.defaults import *

urlpatterns = patterns('Nephaliste.bar.views',
		(r'', 'comptoir'),
		(r'comptoir/$', 'comptoir'),
		(r'boire/$', 'commander'),
		(r'recharger/$', 'crediter'),
)
