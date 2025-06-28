from django.contrib import admin

# Register your models here.
from .models import Produit, Fournisseur, Approvisionnement, Client, Vente
admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Approvisionnement)
admin.site.register(Client)
admin.site.register(Vente)
