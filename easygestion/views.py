from django.shortcuts import redirect, render,get_object_or_404
from django.utils.text import slugify
from .models import Produit,MouvementProduit

def view_home(request):
    produits = Produit.objects.all()
    stat = {
        "labels": ["01/02", "02/02", "03/02", "04/02", "05/02", "06/02", "07/02", "07/03"],
        "stockData": [50, 45, 60, 70, 65, 80, 75, 100]
    }

    return render(request, "easygestion/index.html", context={"produit_liste": produits, "stat": stat})

def view_detail(request,slug):
    produit = get_object_or_404(Produit,slug=slug)
    return render(request,"easygestion/view_product.html",context={"produit":produit})

def view_delete(request,slug):
    produit = get_object_or_404(Produit,slug=slug)
    produit.delete()
    return redirect("easygestion:product")

def product_view(request):
    produits = Produit.objects.all()    
    return render(request,"easygestion/index_one.html",context={"produit_liste":produits})


def add_product_view(request):
    if request.method == "POST":
        nom = request.POST.get("name")
        categorie = request.POST.get("category")
        prix = request.POST.get("price")
        stock = request.POST.get("quantity")
        image = request.FILES.get("image")  # 📌 Gestion du fichier image

        if not nom or not categorie or not prix or not stock:  
            return render(request, "easygestion/add_product.html", {"error": "Tous les champs sont obligatoires."})

        produit = Produit.objects.create(
            nom=nom,
            slug=slugify(nom),
            categorie=categorie,
            prix=float(prix),
            stock=int(stock),
            img=image
        )

        return redirect("easygestion:product")  # Redirection après succès

    return render(request, "easygestion/add_product.html")



def move_view(request):
    mouvements = MouvementProduit.objects.all()
    return render(request, "easygestion/index_two.html", context={"mouvements": mouvements})

def vente_view(request):
    list_info = [
        {
            "img": "https://img.freepik.com/free-photo/transparent-water-bottle-studio_23-2151049138.jpg",
            "produit": "Nom de produit",
            "quantite": 100,
            "prix_total": 2000,
            "date": "12-12-2024"
        },
        {
            "img": "https://img.freepik.com/free-photo/three-green-beer-bottles-with-ears-wheat-wooden-surface_23-2147952050.jpg",
            "produit": "Nom de produit",
            "quantite": 100,
            "prix_total": 2000,
            "date": "12-12-2024"
        },
        {
            "img": "https://img.freepik.com/free-photo/bottle-beer-desk_23-2148600987.jpg",
            "produit": "Nom de produit",
            "quantite": 100,
            "prix_total": 2000,
            "date": "12-12-2024"
        },
        {
            "img": "https://img.freepik.com/free-photo/three-bottles-beer_23-2148600945.jpg",
            "produit": "Nom de produit",
            "quantite": 100,
            "prix_total": 2000,
            "date": "12-12-2024"
        }
    ]
    return render(request, "easygestion/index_three.html", context={"info_table": list_info})

def warning_view(request):
    return render(request,"easygestion/index_four.html")

def add_mouvement_view(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit')
        type_mouvement = request.POST.get('type_mouvement')
        quantite = int(request.POST.get('quantite', 0))
        motif = request.POST.get('motif', '')

        produit = Produit.objects.get(id=produit_id)

        # Calcul du stock restant
        if type_mouvement == 'entrée':
            stock_restant = produit.stock + quantite
        elif type_mouvement in ['sortie', 'retour']:
            if produit.stock >= quantite:
                stock_restant = produit.stock - quantite
            else:
                return render(request, 'easygestion/add_mouvement.html', {
                    'produits': Produit.objects.all(),
                    'error': "Stock insuffisant pour cette sortie."
                })

        # Mise à jour du stock et enregistrement du mouvement
        produit.stock = stock_restant
        produit.save()

        MouvementProduit.objects.create(
            produit=produit,
            type_mouvement=type_mouvement,
            quantite=quantite,
            stock_restant=stock_restant,
            motif=motif
        )

        return redirect('easygestion:move')  # Remplace par ton URL de succès

    produits = Produit.objects.all()
    return render(request, 'easygestion/add_mouvement.html', {'produits': produits})

