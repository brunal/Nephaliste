#encoding=utf-8
from django.shortcuts import render_to_response
from models import *
from forms import *

def comptoir(request, error="", message=""):
	"""
	Cette page liste les boissons disponibles et propose de consommer
	"""
	consommer = ConsommerForm()
	return render_to_response('bar/comptoir.html', {'form': consommer})

	#consommations = Consommation.objects.filter(disponible=True)
	#consommations = sorted(consommations, key=lambda conso: -conso.popularite())
	
	#return render_to_response('bar/comptoir.html', {'consommations': consommations, 'error': error, 'message': message})

def commander(request):
	"""
	Cette page effectue la commande d'une personne (données POST)
	"""
	if not request.method == "POST":
		return comptoir(request, error="Page accessible uniquement en POST")

	#On traite les données reçues

	message=""
	return comptoir(request, message=message)

def crediter(request):
	"""
	Cette page crédite le compte ciblé (données POST)
	"""
	if not request.method == "POST":
		return comptoir(request, error="Page accessible uniquement en POST")

	#On traite les données reçues

	message=""
	return comptoir(request, message=message)
