from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Plat, Entree, Dessert, Boisson


# admin.site.unregister(Plat)
# admin.site.unregister(Entree)
# admin.site.unregister(Dessert)


# Enregistrez les modèles User, Group, Plat, Entree et Dessert dans l'interface d'administration par défaut

from django.contrib.admin import AdminSite

admin.site.site_header = 'Minicucina'
admin.site.site_title = ''
admin.site.index_title = 'Edition de la carte'

# Modèle admin pour gérer l'affichage des Entrees dans l'interface d'administration


@admin.register(Entree)
class EntreeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'jour', 'description')
    ordering = ['id']
    exclude = ('ordre',)


@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'jour', 'description')
    ordering = ['id']
    exclude = ('ordre',)


@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'jour', 'description')
    ordering = ['id']
    exclude = ('ordre',)


@admin.register(Boisson)
class BoissonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'jour', 'description')
    ordering = ['id']
    exclude = ('ordre',)
