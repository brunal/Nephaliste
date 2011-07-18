#coding=utf-8
from django.db import models

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

	solde = models.DecimalField(max_digits=5, decimal_places=2)
	#Date de création du compte
	arrivee = models.DateTimeField(auto_now_add=True)
	#Dernière fois que l'utilisateur a été vu
	depart = models.DateTimeField(auto_now_add=True)
	ouvert = models.BooleanField(default=True)

	#Date d'expiration de la caution
	#Attention : doit être représenté par un booléen côté utilisateur
	caution = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.prenom + " " + self.nom + "(" + self.solde + ", " + self.promotion  + ")"

