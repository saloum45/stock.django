from django.shortcuts import render
from .models import Produit

# Create your views here.

# Afficher la liste des produits
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'stock/liste_produits.html', {'produits': produits})