#encoding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import *

def comptoir(request, error="", message=""):
        """
        Cette page liste les boissons disponibles et propose de consommer
        """
        if request.method == "POST":
                form = ConsommerForm(request.POST)
                if form.is_valid():
                        data = form.cleaned_data
                        historique = form.save()
                        message = u"Consommation : " + unicode(historique)
                        #message = u"Consommation réussie de " + data.consommation + " par " "
                else:
                        message = u"Il y a eu un problème dans le traitement du formulaire."


        consommer = ConsommerForm()

        return render_to_response('bar/comptoir.html', {'form': consommer, 'message': message, 'error': error}, context_instance=RequestContext(request))

#consommations = Consommation.objects.filter(disponible=True)
        #consommations = sorted(consommations, key=lambda conso: -conso.popularite())

        #return render_to_response('bar/comptoir.html', {'consommations': consommations, 'error': error, 'message': message})



def commander(request):
        """
        Cette page effectue la commande d'une personne (données POST)
        Euh ouais en fait c'est comptoir qui fait ca hein
        """
        if not request.method == "POST":
                return comptoir(request, error="Page accessible uniquement en POST")
        else:
                form = ConsommerForm(request.POST)
                if form.is_valid():
                        historique = form.save()
                        message = "Consommation réussie"
                else:
                        message = u"Il y a eu un problème dans le traitement du formulaire."

        return comptoir(request, message=message)

def crediter(request):
        """
        Cette page crédite le compte ciblé (données POST)
        """
        if not request.method == "POST":
                return comptoir(request, error="Page accessible uniquement en POST")
        else:
                form = CrediterForm(request.POST)
                if form.is_valid():
                        solde = form.save()
                        message = u"Dépôt réussi"
                else:
                        message = u"Il y a eu un problème dans le traitement du formulaire."

        return comptoir(request, message=message)


def apercu(request):
        return comptoir(request)
