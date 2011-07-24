#encoding=utf-8
from django import forms
from widgets import *

class ConsommerForm(forms.ModelForm):
	"""
	Formulaire pour la consommation par une personne
	"""
	class Meta:
		model = Historique
#		widgets = {
#				'nom': UserList()
#	}

