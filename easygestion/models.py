from django.db import models
from django.urls import reverse

class Produit(models.Model):
    img = models.ImageField(upload_to="products", blank=True, null=True)
    nom = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    categorie = models.CharField(max_length=128)
    prix = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom} ({self.stock})"

    def get_absolute_url(self):
        return reverse("easygestion:productview", kwargs={"slug": self.slug})

class MouvementProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="mouvements")
    date = models.DateField(auto_now_add=True)
    type_mouvement = models.CharField(
        max_length=50,
        choices=[('entrée', 'Entrée'), ('sortie', 'Sortie'), ('retour', 'Retour')]
    )
    quantite = models.PositiveIntegerField(default=0)  # Quantité ajoutée ou retirée
    stock_restant = models.PositiveIntegerField()
    motif = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.produit.nom} - {self.type_mouvement} - {self.date}"
