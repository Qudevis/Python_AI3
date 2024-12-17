import sqlite3 # importuojame biblioteka darbui su sqlite
database_path = "duomenu_baze.db"
conn = sqlite3.connect(database_path) # atidarome greitkeli

cur = conn.cursor() # sukuriame masina kuri vazines tuo greitkeliu

cur.execute("""
CREATE TABLE IF NOT EXISTS "Users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"age"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
""")

# conn.commit() # Patvirtina uzklausa ir uzsaugo

# def insert_user(name, last_name):
#     cur.execute(f'''Insert into Users(name,last_name)
#              values("{name}","{last_name}")
#             ''')
#     conn.commit() # Sulauzyti pirstus sitam

# def insert_user(name, last_name): # poziciniai parametrai
#     cur.execute(f'''Insert into Users(name,last_name)
#              values(?,?)
#             ''',(name,last_name))
#     conn.commit()

# def insert_user(name, last_name):
#     cur.execute(f'''Insert into Users(name)
#              values(?)
#             ''',(name,))
#     conn.commit()


def insert_user(name, last_name): # vardiniai parametrai
    cur.execute(f'''Insert into Users(name,last_name)
             values(:vardukas,:pavardele)
            ''', {"pavardele": last_name, "vardukas":name})
    conn.commit()

vardas = input("Iveskite varda: ")
pavarde = input("Iveskite pavarde: ")    
insert_user(vardas,pavarde)

# def get_all_users():
#     cur.execute("Select * From Users")
#     return cur.fetchall()
# Update Users Set Name = :Vardas, last_name = :last_name
# def get_all_users():
#     cur.execute("Select * From Users Where name = ?",(reiksme,))
#     return cur.fetchall()

# print(get_all_users())
# conn.close() # uzdarome greitkeli
