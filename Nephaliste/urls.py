from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		(r'^bar/', include('Nephaliste.bar.urls')),
		(r'^compte/', include('Nephaliste.compte.urls')),
		#(r'^', include('Nephaliste.accueil.urls')),

		url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

		url(r'^admin/', include(admin.site.urls)),
		)
