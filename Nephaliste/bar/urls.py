from django.conf.urls.defaults import *

urlpatterns = patterns('Nephaliste.bar.views',
		(r'^$', 'apercu'),
		(r'^comptoir/$', 'comptoir'),
		(r'^boire/$', 'commander'),
		(r'^recharger/$', 'crediter'),
                #(r'^controler/$', 'controler'),
)
