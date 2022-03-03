from django.contrib import admin
from .models import Auteur, Categorie, Editeur, Book

admin.site.register(Auteur)
admin.site.register(Categorie)
admin.site.register(Editeur)
admin.site.register(Book)

# Register your models here.
