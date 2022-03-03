from rest_framework import serializers
from .models import Book, Auteur

class BookSerializer(serializers.ModelSerializer):
    auteur = serializers.StringRelatedField()
    categorie = serializers.StringRelatedField()
    editeur = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = [
            'id',
            'nom',
            'prix',
            'reduction',
            'image',
            'resume',
            'dernier_sold',
            'categorie',
            'auteur',
            'editeur',
        ]