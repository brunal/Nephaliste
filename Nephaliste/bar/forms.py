#encoding=utf-8
from django.forms import ModelForm
from models import Historique
from Nephaliste.compte.models import Depot
from Nephaliste.compte.widgets import ClientsListe

class ConsommerForm(ModelForm):
	"""
	Formulaire pour la consommation par une personne
	"""
	class Meta:
		model = Historique
		widgets = { 'user': ClientsListe() }
