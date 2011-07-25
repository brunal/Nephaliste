#coding=utf-8
from django.db import models
from datetime import datetime, date

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
	user = models.ForeignKey('User')

	def __unicode__(self):
		return u"Dépôt par " + self.user + " de " + self.montant + "€  le " + self.date + " (" + self.get_type_display() + ")"


class Historique(models.Model):
	"""
	Classe retenant toutes les commandes passées
	"""

	user = models.ForeignKey('User')
	consommation = models.ForeignKey('Consommation')
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.consommation + " par " + self.user + " le " + self.date


class Promotion(models.Model):
	"""
	Classe enveloppant un entier : la promotion
	"""
	annee = models.IntegerField()

	def __unicode__(self):
		return self.annee

	def papys(self):
		"""
		Retourne vrai quand les membres de cette promotion ont peu de chance d'être encore à l'école

		>>> from datetime import datetime
		>>> datetime.today().year
		2011
		>>> promo = Promotion.objects.create(annee=2009)
		>>> promo.papys()
		True
		>>> promo2 = Promotion.objects.create(annee=2010)
	>>> promo2.papys()
	False
		"""

		return date.today().year - self.annee.year > 1


class User(models.Model):
	"""
	Classe décrivant un consommateur
	"""
	prenom = models.CharField(max_length=50)
	surnom = models.CharField(max_length=50, blank=True)
	nom = models.CharField(max_length=50)
	email = models.EmailField()

	promotion = models.ForeignKey(Promotion, blank=True, null=True)

	coopeman = models.BooleanField(default=False)

	solde = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	#Date de création du compte
	arrivee = models.DateTimeField(auto_now_add=True)
	#Dernière fois que l'utilisateur a été vu
	depart = models.DateTimeField(auto_now_add=True)
	ouvert = models.BooleanField(default=True)

	#Date d'expiration de la caution
	#Attention : doit être représenté par un booléen côté utilisateur
	caution = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.prenom + " " + self.nom

	def crediter(self, montant, forme):
		"""
		Effectue un dépôt sur le compte d'un consommateur et l'enregistre

		>>> user = User.objects.create(prenom="Hervé", nom="Leguil", email="herve.leguil@supelec.fr")
		>>> user.solde
		0
		>>> user.crediter(10, "liquide")
		>>> user.solde
		10
		"""

		depot = Depot.objects.create(user=self, montant=montant, forme=forme)
		return depot

	def debiter(self, consommation):
		"""
		Débite une boisson à un consommateur
		"""
		commande = Historique.objects.create(user=self, consommation=consommation)
		return commande

	def ajouterCaution(self):
		"""
		Ajoute une caution à un utilisateur
		"""
		self.caution = date.today()
		return

