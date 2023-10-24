from django.db import models
import os
from django.contrib.auth.models import AbstractUser, Group, Permission
from multiselectfield import MultiSelectField


def get_filename(instance, filename):
    return os.path.basename(filename)


class Entree(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='minicucina/static/minicucina/images/entrees/')
    nom_fichier = models.CharField(max_length=100, blank=True, editable=False)
    # Définir les choix pour le champ "jour"
    JOUR_CHOICES = (
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
    )

    # Utiliser le champ CharField avec les choix
    jour = MultiSelectField(max_length=100, choices=JOUR_CHOICES, default=(
        'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'))

    prix = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.nom_fichier = os.path.basename(self.image.name)
        super(Entree, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']  # Tri par l'ID du modèle


class Plat(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='minicucina/static/minicucina/images/plats/')
    nom_fichier = models.CharField(max_length=100, blank=True, editable=False)
    # Définir les choix pour le champ "jour"
    JOUR_CHOICES = (
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
    )

    # Utiliser le champ CharField avec les choix
    jour = MultiSelectField(max_length=100, choices=JOUR_CHOICES, default=(
        'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'))
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.nom_fichier = os.path.basename(self.image.name)
        super(Plat, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']  # Tri par l'ID du modèle


class Dessert(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='minicucina/static/minicucina/images/desserts/')
    nom_fichier = models.CharField(max_length=100, blank=True, editable=False)

    # Définir les choix pour le champ "jour"
    JOUR_CHOICES = (
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
    )

    # Utiliser le champ CharField avec les choix
    jour = MultiSelectField(max_length=100, choices=JOUR_CHOICES, default=(
        'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'))
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.nom_fichier = os.path.basename(self.image.name)
        super(Dessert, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']  # Tri par l'ID du modèle


class Boisson(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='minicucina/static/minicucina/images/boissons/')
    nom_fichier = models.CharField(max_length=100, blank=True, editable=False)

    # Définir les choix pour le champ "jour"
    JOUR_CHOICES = (
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
    )

    # Utiliser le champ CharField avec les choix
    jour = MultiSelectField(max_length=100, choices=JOUR_CHOICES, default=(
        'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi'))
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.nom_fichier = os.path.basename(self.image.name)
        super(Boisson, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']  # Tri par l'ID du modèle
