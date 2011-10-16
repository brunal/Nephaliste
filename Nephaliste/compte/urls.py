from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Nephaliste.compte.views',
                (r'^(?P<compte>.+)/$', 'info'),
                (r'^(?P<compte>.+)/statistiques/$', 'stats'),
                (r'^(?P<compte>.+)/modifier/$', 'editer'),
)
