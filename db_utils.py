import psycopg2

from sys import argv
from psycopg2.errors import *

def connectDB(user, password, dbname):
    connection = psycopg2.connect(port=5432, host="localhost", user=user, password=password, dbname=dbname) 
    cursor = connection.cursor()
    return (cursor)

def displayResult(result, colonnes, table):
    print(table.upper())    
    print(colonnes.upper().replace(",", "\t"))
    for line in result : 
        for colonne in line : 
            print(f"{colonne}\t", end="")
        print("\n")

def getRequestInfo(args):
    colonnes =args[1]
    table = args[-1]

    for i in range(2, len(args)-1):
        colonnes +=f", {args[i]}"
    return (colonnes, table)

def executeRequest(table, colonnes, cursor):
    
    request = f"SELECT {colonnes} FROM \"{table}\""

    try:
        cursor.execute(request)
    except UndefinedColumn : 
        print("le nom de colonne est erroné")
        exit(1)
    except UndefinedTable :
        print("le nom de la table est erroné")
        exit(1)

    result = cursor.fetchall()
    return (result)