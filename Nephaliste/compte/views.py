#encoding=utf-8
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import serializers
from django.http import HttpResponse
from models import *

from math import ceil

def resume(request):
        """
        Résumé : nombre d'utilisateurs, indications pour
        l'utilisateur quant au suivi de son compte
        """
        comptes = User.objects.count()
        ouverts = User.objects.filter(is_active=True).count()

        statut = Ouverture.statut()

        return render_to_response('compte/general.html', 
                        { 'comptes': comptes,
                          'ouverts': ouverts,
                          'statut': statut,
                        }, context_instance=RequestContext(request))


def info(request, compte):
        """
        Dans le futur :
        Avec un paramètre : si l'utilisateur est admin, regarde le compte associé
        Sans paramètre : compte de l'utilisateur ?

        En attendant :
        Compte de la personne
        Idem pour les autres vues
        """

        user = get_object_or_404(User, pk=compte)
        consommations = user.historique_set.order_by('-date')[:5]
        depots = user.depot_set.order_by('-date')[:5]

        return render_to_response('compte/info.html', 
                        { 'user': user,
                          'consos': consommations,
                          'depots': depots,
                        }, context_instance=RequestContext(request))

def stats(request, compte):
        """
        Idem.
        Ou bien stats générales sans paramètre ?
        Il faut alors le sortir de l'application bar/
        """

        return 0

def editer(request, compte):
        """
        Permet à un utilisateur de modifier les informations le concernant
        """
        if request.method == "POST":
                form = CompteForm(request.POST)
                if form.is_valid():
                        data = form.cleaned_data
                        
        return 0

def historique(request, compte, page=1):
        """
        Affiche la liste des consommations d'un utilisateur
        """
        user = get_object_or_404(User, pk=compte)
        page = int(page)
        nombre = user.historique_set.count()

        try:
                historique = user.historique_set.order_by('-date')[20*(page-1):min(20*page,nombre)]
        except User.DoesNotExist:
                raise Http404

        return render_to_response('compte/historique.html',
                        { 'historique': historique,
                          'pages': range(int(ceil(nombre/20))) }, context_instance=RequestContext(request))


def depots(request, compte, page=1):
        """
        Affiche la liste des dépôts d'un utilisateur
        """
        user = get_object_or_404(User, pk=compte)
        page = int(page)
        nombre = user.depot_set.count()

        try:
                depots = user.depot_set.order_by('-date')[20*(page-1):min(20*page,nombre)]
        except User.DoesNotExist:
                raise Http404

        return render_to_response('compte/historique.html',
                        { 'historique': depots,
                          'pages': range(int(ceil(nombre/20))) }, context_instance=RequestContext(request))


def liste(request):
        """
        Renvoie la liste des utilisateurs en JSON
        Utilisé par l'autocomplete
        PUTAIIIIIIIIIIIIIIIIIN
        """
        data = serializers.serialize("json", User.objects.all())
        return HttpResponse(serializers.serialize("json", User.objects.values("username")))
        return HttpResponse(data, mimetype="text/plain")
        # return HttpResponse(data, mimetype="text/json")
