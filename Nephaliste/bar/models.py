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

	def debiter(self, compte):
		"""
		Débite une boisson à un consommateur
		"""
		commande = Historique.objects.create(user=compte, consommation=self)
		return commande


	def __unicode__(self):
		nom = self.nom + u" à " + str(self.prix) + u"€"
		if(not self.disponible):
			nom += " (indisponible)"
		return nom

class Historique(models.Model):
	"""
	Classe retenant toutes les commandes passées
	"""

	user = models.ForeignKey(User)
	consommation = models.ForeignKey('Consommation')
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.consommation) + " par " + unicode(self.user) + " le " + unicode(self.date)
