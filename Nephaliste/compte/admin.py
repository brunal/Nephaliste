#encoding=utf-8
from django.contrib import admin
from models import *
from forms import DeposerForm

class UserAdmin(admin.ModelAdmin):
        list_display = ("username", "first_name", "last_name", "email", "promotion", "is_staff")

class DepotAdmin(admin.ModelAdmin):
        list_display = ("user", "montant", "get_type_display")
        form = DeposerForm

        class Media:
                js = ("admin/jquery.js",)

#admin.site.register(Promotion)
admin.site.register(User, UserAdmin)
admin.site.register(Depot, DepotAdmin)
#admin.site.register(Ouverture)
