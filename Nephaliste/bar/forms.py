#encoding=utf-8
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import RadioSelect
from models import Historique, Consommation
from Nephaliste.compte.models import Depot
from Nephaliste.compte.widgets import ClientsListe

class ConsommerForm(ModelForm):
	"""
	Formulaire pour la consommation par une personne
	"""

	consommation = ModelChoiceField(queryset=Consommation.objects.filter(disponible=True), empty_label=None, widget=RadioSelect)

	class Meta:
		model = Historique
		widgets = { 'user': ClientsListe() }
