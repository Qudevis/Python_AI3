# def hello_world(): # Paruostukas, kuri galiu panaudoti kada noriu
#     print("Labas Pasauli")
#     print("Kaip jums sekasi")
#     print("Kaip jus laikotes ?")

# hello_world()
# hello_world()
# hello_world()

# def say_hello(vardas): # vardas = "Justas"
#     print(f"Labas {vardas}")

# say_hello("Justas kuriam 15 metu 7 9 8 ")

# def suma(skaicius, skaicius2): # skaicius = 7 | skaicius2 = 9
#     rezultatas = skaicius + skaicius2
#     print(f"suma yra {rezultatas}")

# suma(7,9)

# def saraso_suma(sarasas):
#     suma = 0
#     for sk in sarasas:
#         suma += sk
#     print(f"suma yra {suma}")

# mano_sarasas = [7,2,4,5,9,8,7,9,5,1]
# saraso_suma(mano_sarasas)

# def saraso_suma(*skaiciai):
#     suma = 0
#     for sk in skaiciai:
#         suma += sk
#     print(f"suma yra {suma}")

# # mano_sarasas = [7,2,4,5,9,8,7,9,5,1]
# saraso_suma(7,2,4,5,9,8,7,9,5,1) # susikure sarasas ir ji perdave po kapotu

# def suma(skaicius1, skaicius2):
#     rezultatas = skaicius1 + skaicius2
#     print(rezultatas)


# # O kas jeigu norim dar atimti veliau ? Is sumos ?

# skaicius = int(input("Iveskite skaiciu: "))

# suma(skaicius,5) # skaicius = ivesciai, tai cia pasirasys tiesiog skaiciaus reikmse ir gausis suma(7,5)

# # atimtis = skaicius + 5 - 3

# def suma(skaicius1, skaicius2): # skaicius1 = 7
#     rezultatas = skaicius1 + skaicius2 # 7 + 5 | rezultatas = 12
#     return rezultatas # 12


# skaicius = int(input("Iveskite skaiciu: ")) # skaicius = 7 

# grazinta_reiksme = suma(skaicius,5)  # skaicius = 7 vietoje suma atsiranda 12

# print(grazinta_reiksme)

# atimtis = skaicius + 5 - 3

# def funkcija():
#     print("Printiname")
#     return 20

# # print(funkcija()) # funkcija() -> 20 -> print(20)
# funkcija()
# # kint = funkcija() # funkcija() -> 20

# # kint = 20

# print("Kazkas")

# def funkcija():
#     print("Printiname")
#     return 5,9

# kintamasis, kintamasis2 = funkcija() # NEKOREKTISKA
# # kint = None
# # sk = 0
# print(kintamasis)
# paduodamas = "mano sakinys"
#kiek_zodziu(paduodamas)
# kiek_zodziu("Labas vakaras")
# argumentas = "Labas Vakaras"

# def suma(skaicius,skaicius2, skaicius3): # argumentas = "Kazkas", argumentas2 = "Kitas argumentas"
#     print(skaicius + skaicius2+skaicius3)
    # print(argumentas2)

# suma("Kazkas","Kitas argumentas")

# def grazina_10():
#     return [1,5,9,8]

# print(grazina_10()) # grazina_10() -> atsistoja tai, kas yra prie return reiksme
# # siuo atveju print([1,5,9,8])


# def grazina_teksta(tekstas):
#     kint = "Geras kintamasis " + tekstas
#     # bla bla daug kodo
#     return kint # kint -> "Geras kintamasis"

# ivestis = input("Iveskite teksta: ")

# print(grazina_teksta(ivestis))

# def keturkampio_perimetras(L,w):
#     P = L + w + L + w
#     return P

# ilgis = float(input("Iveskite stacakampio ilgi (L)"))

# plotis = float(input("Iveskite stacakampio ploti (w)"))

# gautas_perimetras = keturkampio_perimetras(ilgis,plotis) # gautas_perimetras = P
# print(f"Jusu keturkampio perimetras yra: {gautas_perimetras}")

# def skaiciu_suma(skaicius,skaicius1,skaicius2):
#     suma = skaicius + skaicius1 + skaicius2
#     return suma

# # sk = int(input("iveskite skaiciu: ")) # iveda 15 | sk = 15
# # sk2 = int(input("iveskite skaiciu: ")) 
# # sk3 = int(input("iveskite skaiciu: ")) 

# # grazintas = skaiciu_suma(sk,sk2,sk3) # skaiciu_suma()

# # print(grazintas)

# print(skaiciu_suma(7.5,8.5,9.5))
# print(skaiciu_suma(9,5,4.5))

# sum(["Labas"])

# print(skaiciu_suma("Labas","kaip","sekasi"))



# def skaiciu_suma(skaicius,skaicius1,skaicius2):
#     suma = skaicius + skaicius1 + skaicius2
#     return suma

# sarasas = [4,5,8]
# print(skaiciu_suma(sarasas[0],sarasas[1],sarasas[2]))


# def skaiciu_suma(sarasas):
#     suma = 0
#     for sk in sarasas:
#         suma += sk
#     return suma

# mano_sarasas = [4,5,8]
# print(skaiciu_suma(mano_sarasas))


# def skaiciu_suma(sk1,sk2,sk3=0): # sk1 = 4 | sk2=5 | sk = 0 -> bet jeigu kazka paduodam gaunasi taip sk3 = 6
#     return sk1+sk2+sk3

# print(skaiciu_suma(4,5,6))

# def skaiciu_suma(sk1=0,sk2=0,sk3=0): # sk1 = 4 | sk2=5 | sk = 0 -> bet jeigu kazka paduodam gaunasi taip sk3 = 6
#     return sk1+sk2+sk3

# # print(skaiciu_suma(8,5,7))
# print(skaiciu_suma(8,5))

# def apsipirkti(suma,prekes,ar_reikia_kvito=True):
#     print("Apsipirkimas pavyko")
#     if ar_reikia_kvito:
#         print("Spausdinamas kvitas")

# apsipirkti(15,["Duona,Desreles,Agurkai"])


# def skaiciu_suma(sk1,sk2,sk3=8): # sk1 = 4 | sk2=5 | sk = 0 -> bet jeigu kazka paduodam gaunasi taip sk3 = 6
#     return sk1+sk2+sk3

# # print(skaiciu_suma(8,5,7))
# print(skaiciu_suma(7,5))

# def skaiciu_formule(sk1,sk2=0,sk3=0): # sk1 = 4 | sk2=5 | sk = 0 -> bet jeigu kazka paduodam gaunasi taip sk3 = 6
#     return sk1+sk2*sk3

# print(skaiciu_formule(8,5,7))
# print(skaiciu_formule(6,sk3=4, sk2=7)) # Galimas
# print(skaiciu_formule(sk3=4, sk2=7,6)) # Negalimas


# import datetime as dt

# dt.timedelta(0,0,0,0,0,5) # 5 - tai valandos
# dt.timedelta(hours=5) # 5 - tai valandos

# def skaiciu_suma(*skaiciai): # skaiciai = naujas
#     suma = 0
#     for sk in skaiciai:
#         suma += sk
#     return suma

# print(skaiciu_suma(7,8,9)) # -> naujas = [7,8,9]

# def skaiciu_suma(skaiciai): # skaiciai = naujas
#     suma = 0
#     for sk in skaiciai:
#         suma += sk
#     return suma

# print(skaiciu_suma([7,8,9])) # -> naujas = [7,8,9]


# naujas = []

# while True:
#     ivestis = input("Iveskite skaiciu, kai nebenoresite vesti parasykite q: ")
#     if ivestis == 'q':
#         break
#     naujas.append(int(ivestis))

# print(skaiciu_suma(naujas)) # -> naujas = [7,8,9]

# def skaiciu_suma(sk1,sk2,*skaiciai):
#     return sk1+sk2+sum(skaiciai)

# print(skaiciu_suma(15,9,745,58,78))

# def funkcija(**argumentai):
#     for arg in argumentai.items():
#         print(arg)

# funkcija(Metai=15,Vardas="Jonas")

# def funkcija(argumentai):
#     for arg in argumentai.items():
#         print(arg)

# dict = {"Metai":15,"Vardas":"Jonas"}
# funkcija(dict)

# def saraso_suma(skaiciai):
#     suma = 0
#     for sk in skaiciai:
#         suma += sk
#     return suma

# def daugyba_suma(skaiciai_sumai,daugiklis):
#     return saraso_suma(skaiciai_sumai) * daugiklis

# print(daugyba_suma([7,5,9,5,6],5))



# def grazina_du():
#     return 5,15 # -> naujas_tuple = (5,15)

# kint, kint2 = grazina_du() # (5,15) -> kint = 5 | kint2 = 15

# tuplas = grazina_du()

# print(kint2)


# def kainos_paskaiciavimas(kaina, akcija):
#     # if kaina > 100:
#     #     return kaina * akcija
#     # else:
#     #     return kaina
#     atsakymas = 0
#     if kaina > 100:
#         atsakymas = kaina * akcija

#     else:
#         atsakymas= kaina
#     atsakymas * 5
#     return atsakymas



    
# print(kainos_paskaiciavimas(-5,0.8))

# globalus = 15

# def atspausdink(): # globalus = 10
#     # global globalus
#     globalus = 20 # sukuria nauja kintamaji tik funkcijos ribose globalus ir priskiria = 20
#     # print(lokalus)

# atspausdink()

# print(globalus)

# name = "Global string" # GLOBALUS RANDA IR NAUDOJA

# def greet():
#     name = "Justas" # Enclosing
#     def hello():
#         # name = "Vardas" # LOKALU
#         print(f"Hello {name}")
#     hello()

# greet()
# print(name)

# skaicius = 15

# """
# Komentaras
# nors ne visai komentras
# is tikruju stringas
# """

# tekstas = 'La"bas'
# tekstas2 = "Lab'as"

# didelis_tekstas = '''Labas
# Kaip sekasi
# Grazi diena
# Saule labai sviecia'''

# print(didelis_tekstas)

# def commented_function(kintamasis):
#     """
#     takes an argument and returns it.

#     Args:
#         kintamasis (int): The variable to return.

#     More:
#         kintamasis (int): The variable to return.

#     Returns:
#         int: kintamasis
#     """
#     return kintamasis

# commented_function()

# def kvadratu(sk):
#     return sk **2

# funkcija = lambda sk: sk ** 2

# print(funkcija(7))

# sarasas = [2,4,6,8]

# sarasas2 = map(lambda sk: sk ** 2, sarasas) # sk = sarasas[0]... sk= sarasas[1]

# print(list(sarasas2))

# naujas = []

# for sk in sarasas:
#     naujas.append(kvadratu(sk))

# print(naujas)


# from functools import reduce

# # List of numbers
# numbers = [1, 2, 3, 4, 5]

# # Reduce function to calculate the sum
# result = reduce(lambda x, y: x + y, numbers) # x = 1 y = suma

# print(result)

# # Example: Adding corresponding elements from two lists
# list1 = [1, 2, 3,5]
# list2 = [4, 5, 6]

# # Using map with a lambda that takes two arguments
# result = map(lambda x, y: x + y, list1, list2)

# # Convert the result to a list
# result_list = list(result)

# print(result_list)

# def grazink():
#     return 5,9


# print(grazink())