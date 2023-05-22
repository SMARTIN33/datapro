import credentials

from db_utils import *

def getTotalAchat(id_collecte,cursor):
    query=f"SELECT quantite_produit, prix_unitaire_produit FROM \"Collecte_produit\" WHERE id_collecte ={id_collecte}"
    result=executeQuery(query, cursor)

    total=0
    for line in result:
        total += float (line[0])* float (line[1])
    return(total)

def insertCSP(cursor):
    executeQuery("CREATE TABLE IF NOT EXISTS \"CSP\" (id_categorie INTEGER PRIMARY KEY, nom_categorie VARCHAR(255))", cursor)
    executeQuery("INSERT INTO \"CSP\" VALUES (1, 'ouvriers') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"CSP\" VALUES (2, 'employés') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"CSP\" VALUES (3, 'retraités') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"CSP\" VALUES (4, 'professions intermédiaires') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"CSP\" VALUES (5, 'cadres et professions intellectuelles supérieures') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"CSP\" VALUES (6, 'artisans, commerçants, chefs entreprise')ON CONFLICT DO NOTHING", cursor)

def insertProduit(cursor):
    executeQuery("CREATE TABLE IF NOT EXISTS \"Produit\" (id_produit INTEGER PRIMARY KEY, nom_produit VARCHAR(255))", cursor)
    executeQuery("INSERT INTO \"Produit\" VALUES (1, 'Multimédia') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Produit\" VALUES (2, 'Alimentaire') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Produit\" VALUES (3, 'Maison') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Produit\" VALUES (4, 'Bricolage') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Produit\" VALUES (5, 'Santé') ON CONFLICT DO NOTHING", cursor)

def insertMagasin(cursor):
    executeQuery("CREATE TABLE IF NOT EXISTS \"Magasin\" (id_numero_magasin INTEGER PRIMARY KEY, nom_magasin VARCHAR(255), ville_magasin VARCHAR(255))", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (1, 'Goldenline & CO','Lyon') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (2, 'Goldenline & CO','Nice') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (3, 'Goldenline & CO','Toulouse') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (4, 'Goldenline & CO','Grenoble') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (5, 'Goldenline & CO','La Rochelle') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (6, 'Goldenline & CO','Nantes') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (7, 'Goldenline & CO','Marseille') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (8, 'Goldenline & CO','Strasbourg') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (9, 'Goldenline & CO','Orléans') ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Magasin\" VALUES (10, 'Goldenline & CO','Pau') ON CONFLICT DO NOTHING", cursor)

def insertCollecte(cursor):
    executeQuery("CREATE TABLE IF NOT EXISTS \"Collecte\" (id_collecte INTEGER PRIMARY KEY, date_achat_client timestamp, id_numero_magasin VARCHAR(255))", cursor)
    executeQuery("CREATE TABLE IF NOT EXISTS \"Collecte_produit\" (id_collecte INTEGER, id_produit INTEGER, quantite_produit INTEGER, prix_unitaire_produit double precision, PRIMARY KEY(id_collecte, id_produit, quantite_produit, prix_unitaire_produit))", cursor)
    
    executeQuery("INSERT INTO \"Collecte\" VALUES (1, timestamp '2023-04-10',5) ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Collecte\" VALUES (2, timestamp '2023-04-15',3) ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Collecte\" VALUES (3, timestamp '2023-03-15',2) ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Collecte\" VALUES (4, timestamp '2023-05-01',8) ON CONFLICT DO NOTHING", cursor)

    executeQuery("INSERT INTO \"Collecte_produit\" VALUES (1, 1, 5, 79.95) ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Collecte_produit\" VALUES (1, 2, 8, 80) ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Collecte_produit\" VALUES (2, 1, 10, 100) ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Collecte_produit\" VALUES (2, 2, 15, 82.5) ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Collecte_produit\" VALUES (3, 1, 8, 20) ON CONFLICT DO NOTHING", cursor)
    executeQuery("INSERT INTO \"Collecte_produit\" VALUES (4, 1, 10, 2) ON CONFLICT DO NOTHING", cursor)
   

def insertAchat(cursor):
    executeQuery("CREATE TABLE IF NOT EXISTS \"Achat\" (id_achat INTEGER PRIMARY KEY, nombre_enfant_client INTEGER, id_csp INTEGER, id_collecte INTEGER, total_achat double precision)", cursor)
    executeQuery(f"INSERT INTO \"Achat\" VALUES (1, 5,4,1,{getTotalAchat(1,cursor)}) ON CONFLICT DO NOTHING",cursor)
    executeQuery(f"INSERT INTO \"Achat\" VALUES (2, 2,5,2,{getTotalAchat(2,cursor)}) ON CONFLICT DO NOTHING",cursor)
    executeQuery(f"INSERT INTO \"Achat\" VALUES (3, 3,6,3,{getTotalAchat(3,cursor)}) ON CONFLICT DO NOTHING",cursor)
    executeQuery(f"INSERT INTO \"Achat\" VALUES (4, 0,2,4,{getTotalAchat(4,cursor)}) ON CONFLICT DO NOTHING",cursor)



connection,cursor = connectDB(user=credentials.USER, password=credentials.PASSWORD, dbname=credentials.DBNAME) 


insertCSP(cursor)
insertProduit(cursor)
insertMagasin(cursor)
insertCollecte(cursor)
insertAchat(cursor)

connection.commit()
connection.close()
cursor.close()