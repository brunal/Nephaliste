#coding=utf-8
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, date, timedelta
from Nephaliste.compte.models import User
from exceptions import SoldeInsuffisant

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
        """
        Nombre de commandes de cette consommations sur les sept derniers jours
        """
        popularite = sum(self.historique_set.filter(date__gt=datetime.today() - timedelta(days=7)))
        return popularite

    def __unicode__(self):
        nom = self.nom + u" à " + str(self.prix) + u"€"
        if not self.disponible:
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
        his = unicode(self.consommation) + u" par " + unicode(self.user) 
        if self.date is not None:
            his +=  u" le " + unicode(self.date)
        return his

    def clean(self, *args, **kwargs):
        """
        Vérifie que l'utilisateur a un solde suffisant pour s'offrir la consommation
        """
        super(Historique, self).clean(*args, **kwargs)  #Est-ce nécessaire?
        if not (self.user.solde - self.consommation.prix >= 0  or self.user.hasCaution() and self.consommation.solde - self.consommation.prix >= -25):
            raise ValidationError(u"Solde insuffisant")

    def save(self, *args, **kwargs):
        """
        Enregistre un achat à la Coopé
        On débite donc le compte du consommateur

        TODO: faire attention: est-ce une sauvegarde ou bien une modification?
        """
        self.user.solde -= self.consommation.prix
        super(Historique, self).save(*args, **kwargs)
        self.user.save()
