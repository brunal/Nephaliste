#encoding=utf-8
from django.forms import ModelForm
from django.forms.widgets import RadioSelect
from models import Depot
from widgets import ClientsListe

class DeposerForm(ModelForm):
    """
    Formulaire pour le crédit d'un compte
    """
    class Meta:
        model = Depot
        widgets = { 'user': ClientsListe(),
                    'type': RadioSelect(),
                  }
