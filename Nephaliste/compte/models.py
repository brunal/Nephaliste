#coding=utf-8
from django.db import models
from django.contrib.auth.models import User as U
from datetime import date, timedelta

# Create your models here.


class Promotion(models.Model):
	"""
	Classe enveloppant un entier : la promotion
	"""
	annee = models.IntegerField()

	def __unicode__(self):
		return str(self.annee)

	def isPapy(self):
		"""
		Retourne vrai quand les membres de cette promotion ont peu de chance d'être encore à l'école
                Calcul simple : L'année de la promotion est-elle passée depuis plus d'un an ?

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




class User(U):
	"""
	Classe décrivant un consommateur
        Elle dérive de django.contrib.auth.User, ce qui pose certains problèmes :
        - username est obligatoire, mais pas nom ni prénom
        - un mot de passe est obligatoire

        Les exemples donnés ne sont pas corrects et n'ont pas valeur de test.
	"""
	#prenom = models.CharField(max_length=50)
	#surnom = models.CharField(max_length=50, blank=True)
	#nom = models.CharField(max_length=50)
	#email = models.EmailField()

	promotion = models.ForeignKey(Promotion, blank=True, null=True)

	#coopeman = models.BooleanField(default=False)

	solde = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	#Date de création du compte
	#arrivee = models.DateTimeField(auto_now_add=True)
	#Dernière fois que l'utilisateur a été vu
	depart = models.DateTimeField(auto_now_add=True)
	#ouvert = models.BooleanField(default=True)

	#Date d'expiration de la caution
	#Attention : doit être représenté par un booléen côté utilisateur
	caution = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.first_name + " " + self.last_name

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

	def ajouterCaution(self):
		"""
		Ajoute une caution à un utilisateur
		"""
		self.caution = date.today()
		return

        def hasCaution(self):
                """
                True s'il y a une caution valide,
                False sinon
                """
                return self.caution is not None and date.today() - self.caution < timedelta(days=365)
