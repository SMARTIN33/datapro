from sys import argv
from db_utils import *
import credentials
from random import randint
from datetime import date
from generate_dataset import insertProduit
import requests


def dataset_tests():
    connection,cursor = connectDB(user=credentials.USER, password=credentials.PASSWORD, dbname=credentials.DBNAME) 

    executeQuery("CREATE TABLE \"DATASET_TEST\" (id INTEGER PRIMARY KEY, nom VARCHAR(255), date timestamp)", cursor)

    id=str(randint(1,2000))
    today=date.today()
    executeQuery(f"INSERT INTO \"DATASET_TEST\" VALUES ({id}, 'test', timestamp '{today}')", cursor)
    connection.commit()

    result=executeQuery(f"SELECT * FROM \"DATASET_TEST\" WHERE id={id}", cursor)
    if len(result)==0:
        executeQuery("DROP TABLE IF EXISTS \"DATASET_TEST\"", cursor)
        connection.commit()
        return False 
    executeQuery("DROP TABLE IF EXISTS \"Produit\"", cursor)
    connection.commit()
    insertProduit(cursor)
    connection.commit()
    result=executeQuery("SELECT * FROM \"Produit\"", cursor)
    if len(result)==0:
        return False 
    return True

def export_tests():
    connection,cursor = connectDB(user=credentials.USER, password=credentials.PASSWORD, dbname=credentials.DBNAME) 
    response=requests.post("http://127.0.0.1:8000/chart/download?number=2")
    if response.status_code != 200:
        return False
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'Achat' order by ordinal_position")
    column_name=cursor.fetchall()
    column_name = [elem[0] for elem in column_name]
    for name in column_name:
        if name not in response.content.decode("utf-8"):
            return False
    return True


def main():
    if len(argv)==1:
        print(f"utilisation : {argv[0]} [dataset|export]")
        return 
    initial=argv[1][0].lower()
    result=None
    match initial:
        case "d":
            result=dataset_tests()
        case "e":
            result=export_tests()
        case _:
            print(f"utilisation : {argv[0]} [dataset|export]")

    if result is not None and result==True:
        print("Le test a bien été exécuté.")
    else:
        print("Le test n'a pas bien été exécuté.")

main()