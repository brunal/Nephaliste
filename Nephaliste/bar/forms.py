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

class CrediterForm(ModelForm):
        """
        Formulaire pour le crédit d'un compte
        """
        class Meta:
                model = Depot
