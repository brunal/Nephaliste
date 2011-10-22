from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Nephaliste.compte.views',
                (r'^$', 'resume'),
                (r'^(?P<compte>.+)/$', 'info'),
                (r'^(?P<compte>.+)/consommations/(?P<page>.+)$', 'historique'),
                (r'^(?P<compte>.+)/depots/(?P<page>.+)$', 'depots'),
                (r'^(?P<compte>.+)/statistiques/$', 'stats'),
                (r'^(?P<compte>.+)/modifier/$', 'editer'),

                (r'^liste$', 'liste'),
)
