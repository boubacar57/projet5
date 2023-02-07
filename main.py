import sqlite3
with sqlite3.connect("contacss.db ") as connection:
    cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS depenses(loyer INTEGER, manger INTEGER , transport INTEGER)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS revenus(salaire INTEGER, business INTEGER )")
def enrigistrer_depenses():
    print("Enrigistrer vos depenses")
    loyer = input("Entrer votre loyer")
    manger = input("Entrer votre manger")
    transport = input("Entrer votre transport")
    cursor.execute("INSERT INTO depenses(loyer)VALUES(?)",(loyer,))
    cursor.execute("INSERT INTO depenses(manger)VALUES(?)", (manger,))
    cursor.execute("INSERT INTO depenses(transport)VALUES(?)", (transport,))
    connection.commit()
    print("depenses enrigidstrer avec succes!")

def enrigistrer_revenus():
    print("Enrigistrer vos revenus")
    salaire = input("Entrer votre salaire")
    business = input("Entrer votre business")
    cursor.execute("INSERT INTO revenus(salaire)VALUES(?)",(salaire,))
    cursor.execute("INSERT INTO revenus(business)VALUES(?)", (business,))
    connection.commit()
    print("revenus enrigidstrer avec succes!")

def menu_principal():
    choix = ""
    print("---------------------------------")
    print("-------Gestion des budgets-------")
    print("    1.Enrigistrer vos dépenses")
    print("    2.Enrigistrer vos revenus")
    print("    3.Quitter l'application")
    print("---------------------------------")
    choix= input("choisir votre références !\n")
    if choix == "1":
        enrigistrer_depenses()
        menu_principal()
    elif choix == "2":
        enrigistrer_revenus() 
        menu_principal()
    elif choix == "3":
        print("Quitter l'application")
        exit()
    else:
        print("choix invalide!")
        exit()
menu_principal()


