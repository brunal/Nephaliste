#encoding=utf-8
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def info(request, compte):
        """
        Dans le futur :
        Avec un paramètre : si l'utilisateur est admin, regarde le compte associé
        Sans paramètre : compte de l'utilisateur ?

        En attendant :
        Compte de la personne
        Idem pour les autres vues
        """

        user = ''

        return render_to_response('compte/info.html', {'user': user})

def stats(request, compte):
        """
        Idem.
        Ou bien stats générales sans paramètre ?
        Il faut alors le sortir de l'application bar/
        """

        return 0

def editer(request, compte):
        return 0
