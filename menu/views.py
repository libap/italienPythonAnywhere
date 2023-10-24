from django.shortcuts import render
from .models import Plat, Entree, Dessert, Boisson
from datetime import datetime
import locale

# Create your views here.


def acceuil_home(request):

    entrees = Entree.objects.all()
    plats = Plat.objects.all()
    desserts = Dessert.objects.all()
    boissons = Boisson.objects.all()

    jours_semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
    classes = {
        'entrees': entrees,
        'plats': plats,
        'desserts': desserts,
        'boissons': boissons,
        # Ajoutez d'autres classes au besoin
    }

    # Définir la locale française
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

    # Obtenir le jour actuel en français pour l'affichage
    current_day = datetime.now().strftime('%A')

    return render(request, 'acceuil_menu.html', {'entrees': entrees, 'plats': plats, 'desserts': desserts, 'boissons': boissons, 'current_day': current_day, 'jours_semaine': jours_semaine, 'classes': classes})
