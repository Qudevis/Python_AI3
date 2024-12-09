# # 7/0

# # int("Labas")
# print("Pirmas")
# # daliklis = 0


# while True:
#     try:
#         daliklis = int(input("Prasau ivesti dalikli"))
#         7/daliklis # ivyko klaida, ir cia galite isivaizduoti tarsi cikle ivyko break
#         print("Veikiu po dalyba")
#         break
#     except:
#         print("Ivyko klaida megink dar karta")
        

# print("veikiu po try except")
# tuplas = (4,9,8,7)
# tuplas[0] = 5
# try:
#     # tuplas = (4,9,8,7)
#     # tuplas[0] = 5
#     7/0
#     # int("Labas")
# except ZeroDivisionError as ex: # sitas gaudys tik dalyba is nulio ir ex prisiims klaidos teksta; ex = klaidos tekstas
#     print(ex)
# except ValueError:
#     print("NEgalima konvertuoti teksto i skaiciu")
# except TypeError:
#     print("Nutiko tuple klaida")
# except:
#     print("Ivyko kazkas netiketo")

# 7/0 # Nuo sitos vietos programa sustoja ir yra nutraukiama su negrazia klaida
# try:
    
#     ivestis = float(input("Iveskite skaiciu: "))

#     7/ivestis

#     open("Netikras.txt")
#     print(ivestis)
#     print("Try pasieke pabaiga")
# except ValueError: # Gaudo netinkamos reiksmes klaidas
#     print("Ivedete ne skaiciu")
# except ZeroDivisionError: # Gaudo dalybos is nulio klaidas
#     print("DAlyba is nulio negalima")
# except: # Gaudo visas klaidas 
#     print("Ivyko klaida")

# print("Programa veikia toliau")


# try: # isorinis
#     print("Pirmas try")
#     # 7/0 # Nuo sitos vietos try nutraukiamas

#     try: # vidinis
#         print("Antras try")
#         7/0
#     except ValueError: # sitas priklauso vidiniam try
#         print("Antro except printas")
    
#     # 7/0 # uz vidinio try/except ribu

# except: # Sitas priklauso isoriniam try
#     print("Pirmo try exceptas")

# print("Programa veikia toliau")
# 7/0

# try:
#     7/0
# except:
#     print("")


# try:
#     7/0
#     print("Try vyksta toliau")
# except ZeroDivisionError as ex:
#     print(ex)
#     # print("dalyba is nulio negalima")

# import traceback

# try:

#     7 / 0  
# except Exception as e:
#     print(e)

#     tb = traceback.extract_tb(e.__traceback__)
#     print(tb)
#     for frame in tb:
#         print(f"{frame.filename}, {frame.lineno}")

# I loga idek laika idek eilute idek pacia klaida 


# try:
#     pass
# except:
#     pass
# finally:
#     pass

# try:
#     failas = open("Blabla.txt") 
#     failas.read()#.....
#     # dar kazkokiu veiksmu
# except:
#     print("Ivyko klaida")    
# finally: # Ivyks nesvarbu ar ivyko klaida ar neivyko VISADOS VYKDOMAS
#     failas.close()

# raise - paskirtis iskelti klaida

# daliklis = int(input("iveskite dalikli: ")) # - gaunam dalikli

# try:
#     if daliklis == 0:
#         raise ZeroDivisionError("Negalima nurodyti daliklio is nulio ")
#     else:
#         print(f"atsakymas {7/daliklis}")
# except Exception as ex:
#     print(f"Mano klaida yra: {ex}")