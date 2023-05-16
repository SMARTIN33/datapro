import psycopg2
from sys import argv
connection = psycopg2.connect(port=5432, host="localhost", user="postgres", password="RogerRafa1523", dbname="DB Goldenline") 

cursor = connection.cursor()

colonnes =argv[1]
table = argv[-1]

for i in range(2, len(argv)-1):
    colonnes +=f", {argv[i]}"

print(colonnes)

request = f"SELECT {colonnes} FROM \"{table}\""

cursor.execute(request)

result = cursor.fetchall()
print(table.upper())    
print(colonnes.upper().replace(",", "\t"))

for line in result : 
    for colonne in line : 
        print(f"{colonne}\t", end="")
    print("\n")