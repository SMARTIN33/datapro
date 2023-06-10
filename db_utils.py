import psycopg2

from sys import argv
from psycopg2.errors import *

def connectDB(user, password, dbname, host, port):
    
    """"Permet de se connecter entre la base de données postgreSQL & python. 
    Les éléments importants à notifier sont : le numéro de port, le type d'hébergeur, le nom de l'utilisateur, le mot de passe et le nom de la base de données."""

    connection = psycopg2.connect(port=port, host=host, user=user, password=password, dbname=dbname) 
    cursor = connection.cursor()
    return (connection, cursor)

def displaySelectResult(result, colonnes, table):
    
    """"Permet d'afficher le résultat de la recherche. 
    Nous demandons à afficher les tables et les colonnes de la base de données en séparant les colonnes par une tabulation. 
    Chaque nom des colonnes sera affiché en majuscule. 
    A la fin de chaque ligne, nous avons effectué un retour à la ligne."""

    print(table.upper())    
    print(colonnes.upper().replace(",", "\t"))
    for line in result : 
        for colonne in line : 
            print(f"{colonne}\t", end="")
        print("\n")

def getQueryInfo(args):

    """"Permet d'obtenir des informations concernant la requête.
    On récupérer les colonnes à partir de 'args'. 
    'args' permettra de passer un nombre indéfini d'arguments lors de l'appel de la fonction."""

    colonnes =args[1]
    table = args[-1]

    for i in range(2, len(args)-1):
        colonnes +=f", {args[i]}"
    return (colonnes, table)

def executeSelectQuery(table, colonnes, cursor):
    
    """"Permet d'exécuter la requête. 
    Cette requête va sélectionner les différents champs provenant de la table appelée.
    Lors de l'exécution de la requête, si le nom de la colonne ou le nom de la table sont erronés, alors un message d'erreur sera affiché sinon la requête s'affichera correctement."""

    query = f"SELECT {colonnes} FROM \"{table}\""

    try:
        cursor.execute(query)
    except UndefinedColumn : 
        print("le nom de colonne est erroné")
        exit(1)
    except UndefinedTable :
        print("le nom de la table est erroné")
        exit(1)

    result = cursor.fetchall()
    return (result)


def executeQuery(query,cursor):

    """"Permet d'exécuter la requête.
    Lors de l'exécution de la requête, si le nom de la colonne ou le nom de la table sont erronés, alors un message d'erreur sera affiché sinon la requête s'affichera correctement."""

    try:
        cursor.execute(query)
    except UndefinedColumn : 
        print("le nom de colonne est erroné")
        return(None)
    except UndefinedTable :
        print("le nom de la table est erroné")
        return(None)
    
    if (cursor.description) is not None:
        return cursor.fetchall()
    else :
        return(None)

def displayResult(result):
    
    """"Permet d'afficher le résultat de la recherche. 
    A la fin de chaque ligne, nous avons effectué un retour à la ligne."""

    for line in result : 
        for colonne in line : 
            print(f"{colonne}\t", end="")
        print("\n")