from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template import loader, Context
from .models import *
from django.db import connection
from django.shortcuts import *
import os
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):

    """"Affiche un dashboard dynamique en fonction du statut de la base de données."""

    depenses=[]
    catgories_csp=[]
    nombre_achats=[]
    number_commands=0
    number_products=0
    revenue=0
    with connection.cursor() as cursor: 
        cursor.execute("SELECT COUNT(id_achat) FROM \"Achat\"")
        number_commands=cursor.fetchone()[0]
        cursor.execute("SELECT sum (quantite_produit) from \"Collecte_produit\"")
        number_products=cursor.fetchone()[0]
        cursor.execute("SELECT sum (total_achat) from \"Achat\"")
        revenue=cursor.fetchone()[0]

  
        for i in range (1,6) :
            cursor.execute("SELECT sum(total_achat) from \"Achat\" INNER JOIN \"CSP\" ON \"CSP\".id_categorie = \"Achat\".id_csp WHERE id_categorie = %s", str(i))
            ligne=cursor.fetchone()
            depenses.append(ligne)
          
            cursor.execute("SELECT nom_categorie FROM \"CSP\" WHERE id_categorie = %s", str(i))
            ligne=cursor.fetchone()
            catgories_csp.append(ligne)

            cursor.execute("SELECT count (id_achat) FROM \"Achat\" WHERE id_csp = %s", str(i))
            ligne=cursor.fetchone()
            nombre_achats.append(ligne)

        depenses = [elem[0] if elem[0] is not None else 0 for elem in depenses]
        catgories_csp = [elem[0] for elem in catgories_csp]
        nombre_achats = [elem[0] if elem[0] != 0 else 1 for elem in nombre_achats]
        paniers_moyens= [] 

        for i in range (5) :
            paniers_moyens.append(depenses[i]/nombre_achats[i])

    total=(Achat.objects.filter(id_csp=1).only("total_achat"))
    context=Context({"depenses":depenses, "categories": catgories_csp, "paniers_moyens" : paniers_moyens, "number_commands": number_commands, "number_products": number_products, "revenue": revenue})
    template=loader.get_template('chart.html')
    return HttpResponse(template.render(context.flatten()))

@csrf_exempt
def download (request):

    """"Télécharge un fichier csv contenant un nombre de ligne précisé par l'utilisateur, de la table Achat."""

    lignes, column_name=getAchatData(request.GET.get("number"))
    f=serialize_data("export_data_collecte.csv", column_name, lignes)
    filename=f.name
    f.close()
    response=FileResponse(open("export_data_collecte.csv", "rb"))
   
    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
   
    return response
    

def getAchatData (limit):

    """"Récupére les 'limit' premières lignes de la table Achat dans la base de données."""

    lignes= []
    column_name=[]
    with connection.cursor() as cursor: 
        cursor.execute("SELECT * from \"Achat\" LIMIT %s",limit)
        lignes=cursor.fetchall()
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'Achat' order by ordinal_position")
        column_name=cursor.fetchall()
    column_name = [elem[0] for elem in column_name]
    return (lignes, column_name)


def serialize_data(filename, column_name, lignes):

    """ Sérialise les 'lignes' de la base de données sous le format 'column_name' dans un fichier csv nommé 'filename". """

    f=open(filename, "w")
    for column in column_name:
        f.write(column)
        f.write(";")
    f.write("\n")
    for l in lignes :
        for c in l:
            f.write(str(c))
            f.write(";")
        f.write("\n")
    return(f)