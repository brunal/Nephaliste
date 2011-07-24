#encoding=utf-8
from django.forms import *

class UserList(TextInput):
	"""
	Un widget avec liste pseudo-déroulante (lié à la présence de Javascript...)
	"""
	def decompress(self, value):
		#Récupérer l'utilisateur dont le nom correspond
		return value
