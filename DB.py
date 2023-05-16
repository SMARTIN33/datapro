import psycopg2
from sys import argv
from psycopg2.errors import *
if len(argv) < 3 :
    print ("Nous ne pouvons donner suite à votre demande : nombre insuffisant d'argument donné. Nous avons besoin au minimum d'une colonne et d'une table.")
    exit (1)

connection = psycopg2.connect(port=5432, host="localhost", user="postgres", password="RogerRafa1523", dbname="DB Goldenline") 

cursor = connection.cursor()

colonnes =argv[1]
table = argv[-1]

for i in range(2, len(argv)-1):
    colonnes +=f", {argv[i]}"

print(colonnes)

request = f"SELECT {colonnes} FROM \"{table}\""

try:
    cursor.execute(request)
except UndefinedColumn : 
    print("le nom de colonne est erroné")
    exit(1)

result = cursor.fetchall()
print(table.upper())    
print(colonnes.upper().replace(",", "\t"))

for line in result : 
    for colonne in line : 
        print(f"{colonne}\t", end="")
    print("\n")