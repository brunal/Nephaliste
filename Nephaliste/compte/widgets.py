#coding=utf-8
from django.forms import TextInput

class ClientsListe(TextInput):
        attr = { 'class': 'clientsListe' }
        class Media:
                css = {
                                'all': ('jqueryui/css/jquery-ui-1.8.16.custom.css',)
                                }
                js = ('jqueryui/js/jquery-ui-1.8.16.custom.min.js', 'compte/clientsListe.js')
