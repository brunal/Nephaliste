#coding=utf-8
from django.forms import TextInput
from models import User

class ClientsListe(TextInput):
    """
    Un widget avec liste pseudo-déroulante (lié à la présence de Javascript)
    """

    attr = { 'class': 'clientsListe' }

    def value_from_datadict(self, data, files, name):
        value = super(ClientsListe, self).value_from_datadict(data, files, name) #data.get(name)
        return User.objects.get(username=value).id

    def render(self, name, value, attrs=None):
        username = User.objects.get(id=value).username
        return super(ClientsListe, self).render(name, username, attrs)

    class Media:
        css = {
                'all': ('jqueryui/css/jquery-ui-1.8.16.custom.css',)
              }
        js = ('jqueryui/js/jquery-ui-1.8.16.custom.min.js', 'compte/clientsListe.js')
