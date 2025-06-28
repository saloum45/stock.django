from django.db import models

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()

    def __str__(self):
        return self.nom

class Approvisionnement(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.produit.stock += self.quantite
        self.produit.save()
        super().save(*args, **kwargs)

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    quantite = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.produit.stock >= self.quantite:
            self.produit.stock -= self.quantite
            self.produit.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Stock insuffisant")
