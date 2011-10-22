#coding=utf-8


from django.forms import TextInput

class ClientsListe(TextInput):
        attr = { 'class': 'clientsListe' }
        class Media:
                js = ('compte/jquery.autocomplete.pack.js', 'compte/clientsListe.js')
