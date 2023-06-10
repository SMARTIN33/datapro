from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template import loader, Context
from .models import *
from django.db import connection
from django.shortcuts import *


# Create your views here.

def index(request):

    total=0
    depenses_categorie=[]
    categories_produit=[]
    id_collecte=0
    id_achat="1" if request.GET.get("id_achat") is None else request.GET.get("id_achat")

    with connection.cursor() as cursor: 
        cursor.execute("SELECT total_achat FROM \"Achat\" WHERE id_achat= %s", id_achat)
        total=cursor.fetchone()[0]
        cursor.execute("SELECT id_collecte FROM \"Achat\" WHERE id_achat= %s", id_achat)
        id_collecte=cursor.fetchone()[0]
        cursor.execute("SELECT nom_produit, prix_unitaire_produit, quantite_produit from \"Collecte_produit\" JOIN \"Produit\" ON \"Collecte_produit\".id_produit=\"Produit\".id_produit where id_collecte= %s", str(id_collecte))
        for ligne in cursor.fetchall():
            categories_produit.append(ligne[0])
            depenses_categorie.append(int(ligne[2])*float(ligne[1]))



    context=Context({"categories":categories_produit, "depenses":depenses_categorie, "total_achat":total})
    template=loader.get_template('details.html')
    return HttpResponse(template.render(context.flatten()))