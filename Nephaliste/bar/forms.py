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
		widgets = {
				'user': ClientsListe()
                }

class CrediterForm(ModelForm):
        """
        Formulaire pour le crédit d'un compte
        """
        class Meta:
                model = Depot
