#coding=utf-8
from django.db import models
from datetime import datetime, date
from Nephaliste.compte.models import User

class Consommation(models.Model):
	"""
	Chaque objet est une chose que la Coopé vend

	>>> conso = Consommation.objects.create(nom="Pinte de Kro", prix="2.00")
	>>> conso
	'Pinte de Kro à 2.00€'

	"""

	nom = models.CharField(max_length=50)
	disponible = models.BooleanField(default=True)
	prix = models.DecimalField(max_digits=4, decimal_places=2)

	def popularite(self):
		popularite = sum(self.historique_set.filter(date__gt=datetime.today()))
		return popularite

	def __unicode__(self):
		nom = self.nom + u" à " + self.prix + u"€"
		if(not self.disponible):
			nom += " (indisponible)"
		return nom

class Depot(models.Model):
	"""
	Classe retenant l'argent déposé par un client
	"""
	TYPES = (
			(0, u'cash'),
			(1, u'chèque'),
			)
	type = models.IntegerField(choices=TYPES)
	date = models.DateTimeField(auto_now_add=True)
	montant = models.DecimalField(max_digits=5, decimal_places=2)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return u"Dépôt par " + self.user + " de " + self.montant + "€  le " + self.date + " (" + self.get_type_display() + ")"


class Historique(models.Model):
	"""
	Classe retenant toutes les commandes passées
	"""

	user = models.ForeignKey(User)
	consommation = models.ForeignKey('Consommation')
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.consommation + " par " + self.user + " le " + self.date
