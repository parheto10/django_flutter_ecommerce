from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self):
        return ('%s') %(self.nom)

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self):
        return ('%s') %(self.nom)

class Editeur(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self):
        return ('%s') %(self.nom)

class Book(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.PositiveIntegerField(default=0)
    reduction = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True)
    resume = models.FileField(null=True)
    dernier_sold = models.DateTimeField(null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, null=True)
    auteur = models.ForeignKey(Auteur, on_delete=models.PROTECT, null=True)
    editeur = models.ForeignKey(Editeur, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return ('%s - %s') %(self.nom, self.auteur.nom)

# Create your models here.
