#encoding=utf-8
from django.shortcuts import render_to_response
from models import *

def comptoir(request):
	"""
	Cette page liste les boissons disponibles et propose de consommer
	"""
	consommations = Consommation.objects.filter(disponible=True)
	consommations = sorted(consommations, key=lambda conso: -conso.popularite())
	
	return render_to_response('bar/comptoir.html', {'consommations': consommations})
