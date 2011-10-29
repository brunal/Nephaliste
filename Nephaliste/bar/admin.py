#encoding=utf-8
from django.contrib import admin
from models import *
from forms import ConsommerForm

class HistoriqueAdmin(admin.ModelAdmin):
        list_display = ('user', 'consommation', 'date')
        list_display_links = list_display
        form = ConsommerForm

        class Media:
                js = ("admin/jquery.js",)

class ConsommationAdmin(admin.ModelAdmin):
        list_display = ('nom', 'prix', 'disponible', 'popularite')

admin.site.register(Consommation, ConsommationAdmin)
admin.site.register(Historique, HistoriqueAdmin)
