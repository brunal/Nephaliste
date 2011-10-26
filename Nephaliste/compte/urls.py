from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Nephaliste.compte.views',
                (r'^$', 'resume'),
                (r'^(?P<compte>\d+)/info/$', 'info'),

                (r'^(?P<compte>\d+)/consommations/$', 'historique'),
                (r'^(?P<compte>\d+)/consommations/(?P<page>\d+)$', 'historique'),

                (r'^(?P<compte>\d+)/depots/$', 'depots'),
                (r'^(?P<compte>\d+)/depots/(?P<page>\d+)$', 'depots'),

                (r'^(?P<compte>\d+)/statistiques/$', 'stats'),
                (r'^(?P<compte>\d+)/modifier/$', 'editer'),

                (r'^liste$', 'liste'),
)
