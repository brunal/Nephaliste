#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User as U, UserManager
from datetime import date, datetime, timedelta


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

        #cf http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance/
        objects = UserManager()

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
        def derniere_visite(self):
                """
                Renvoie la dernière mention du compte de la personne dans la DB?
                Problème : dépendance envers l'app bar -> circulaire...
                Solution: màj à chaque save()

                Sauf qu'en fait ca existe déja dans Django... utiliser ca
                """
                return self.last_login



class Depot(models.Model):
	"""
	Classe retenant l'argent déposé par un client
	"""
	TYPES = (
			(0, u'cash'),
			(1, u'chèque'),
			)
	type = models.IntegerField(choices=TYPES, default=0)
	date = models.DateTimeField(auto_now_add=True)
	montant = models.DecimalField(max_digits=5, decimal_places=2)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return u"Dépôt par " + self.user.username + u" de " + unicode(self.montant) + u" €  le " + unicode(self.date) + u" (" + self.get_type_display() + u")"


class Ouverture(models.Model):
        """
        Classe disant si la Coopé est ouverte, et récapitulant
        quand elle l'a été
        """
        ouverture = models.DateTimeField(auto_now_add=True)
        fermeture = models.DateTimeField(blank=True, null=True)

        def save(self):
                """
                Sauve un nouvel objet Ouverture
                Si un objet Ouverture précédent existe avec fermeture = false,
                alors il est fermé avec la dernière date présente (dans dépôt
                ou dans historique)
                """
                dernier = Ouverture.objects.latest()
                if dernier.fermeture is None:
                        #La Coopé n'a pas été fermée
                        #TODO: déterminer la date de fermeture
                        dernier.fermeture = datetime.datetime.now()
                        dernier.save(force_update=True)

                super(Ouverture, self).save()
                #models.Model.save(self)

        @staticmethod
        def statut():
                """
                Renvoie le statut actuel de la Coopé
                True : ouverte
                False : fermée
                """
                dernier = Ouverture.objects.latest()
                return dernier.fermeture is None

        def __unicode__(self):
                u =  u"Ouvert le " + unicode(self.ouverture)
                if self.fermeture is not None:
                        u += " et fermé le " + unicode(self.fermeture)
                return u

        class Meta:
                get_latest_by = "ouverture"
