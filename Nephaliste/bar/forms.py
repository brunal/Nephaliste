#encoding=utf-8
from django.forms import ModelForm
from models import Historique
#from widgets import *

class ConsommerForm(ModelForm):
	"""
	Formulaire pour la consommation par une personne
	"""
	class Meta:
		model = Historique
#		widgets = {
#				'nom': UserList()
#	}

