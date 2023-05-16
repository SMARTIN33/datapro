import credentials

from db_utils import *
from sys import argv

if len(argv) < 3 :
    print ("Nous ne pouvons donner suite à votre demande : nombre insuffisant d'argument donné. Nous avons besoin au minimum d'une colonne et d'une table.")
    exit (1)

cursor = connectDB(user=credentials.USER, password=credentials.PASSWORD, dbname=credentials.DBNAME) 
colonnes, table = getRequestInfo(argv)
result = executeRequest(table, colonnes, cursor)

displayResult(result, colonnes, table)