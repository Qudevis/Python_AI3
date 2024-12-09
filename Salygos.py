# ar_tiesa = bool("True")

# ar_tiesa = True
# ar_tiesa2 = False

# print(5==4) # ar lygu

# print(5 != 4) # ar nelygu

# print(8 <= 8) # maziau arba lygu

# print(7 == 7 and 4 > 3 and 7 >= 8) # su and visos salygos turi buti teisingos

# print((7==5 and 4 > 5) or (6 > 5 and 4 > 3)) 

# ar_tiesa = 7 > 3
# print(ar_tiesa)

# age = int(input("Iveskite savo amziu "))

# if age > 18: # -> (age > 18) -> True/False
#     print("Tu jau esi pilnametis")
#     print("Tu jau esi pilnametis")
#     print("Tu jau esi pilnametis")
#     print("Tu jau esi pilnametis")
#     print("Tu jau esi pilnametis")
#     vardas = input("Ivesk savo varda: ")

# print("Visada veikiu")

#     # print("As jau nebesu ife") # Jau nebepriklauso ifui

# if 4 > 3:
#     pass # pass tai vietos laikiklis, kazkam kitam, kad leistu paleisti programa nes ifas negali buti tuscias
# print("Kazkas")

# if 8 > 4: # Ifas gali tureti ifus
#     print("Pirmas tiesa")
#     if 7 > 3:
#         print("Antras irgi tiesa")
#         if 5 > 6:
#             print("Trecias irgi tiesa")
#             if 8 > 4:
#                 print("Pirmas tiesa")
#                 if 7 > 3:
#                     print("Antras irgi tiesa")
#                     if 5 > 6:
#                         print("Trecias irgi tiesa")

# age = int(input("Iveskite savo amziu: "))


# if age >= 16:
#     print("gali eiti i siaubo filma")
# else:
#     pass


# if age >= 18:
#     print("Tu gali nusipirkti energetini")
# else:
#     print("Tu dar per jaunas")

# if age >= 18: # Netiesa jeigu 7 metu
#     print("Tu jau pilnametis")
# elif age >= 3: # Tiesa jeigu 7 metu
#     print("Gali delioti delione")
# elif age > 6: # # Tiesa jeigu 7 metu, bet iki sito mes nedaeiname
#     print("Tu jau eini i mokykla")
# elif age > 9:
#     print("IRGI TIESA")

# if age >= 18: # 18 ir daugiau
#     print("Tu jau pilnametis")
# elif age >= 3 and age < 6: # 3 4 5
#     print("Gali delioti delione")
# elif age > 6 and age <= 9:  # 7 8
#     print("Tu jau eini i mokykla")
# elif age > 9 and age < 18: # 10-17 (imtinai)
#     print("IRGI TIESA")
# age = int(input("Iveskite savo amziu: "))

# if age >= 18 and age < 65: # 18 ir daugiau bet maziau nei 65
#     print("Tu jau pilnametis")
# elif age >= 3 and age < 6: # 3 4 5
#     print("Gali delioti delione")
# elif age > 6 and age <= 9:  # 7 8
#     print("Tu jau eini i mokykla")
# elif age > 9 and age < 18: # 10-17 (imtinai)
#     print("IRGI TIESA")
# else:
#     print("Nei vienas nebuvo tiesa")

# text = "Mano tekstas labai geras"
# text = text.upper()
# if text.istitle(): # isupper -> true arba false # Ifo kodas vykdomas tada, kai yra True, nevykdomas kai yra False
#     print("Tekstas yra didziosiom raidem")
# else:
#     print("Tekstas turi mazuju raidziu")

# import this

# text = "Mano tekstas labai geras"

# zodziai = text.split()

# print(zodziai[-1][-2])

# print(zodziai)

age = int(input("Iveskite amziu: "))

match age:
    case 8: # age == 8.... techniskai galima tikrinti ar age > 8
        print("Tau astuoneri")
    case 18:
        print("Tau astuonolika")
    case 30:
        print("Tau trisdesimt")
    case _: # else
        print("Nezinau kiek tau")

    # if age == 8:
    #     print("Tau astuoneri")
    # elif age == 18:
    #     print("Tau astuonolika")
    # else _:
    #     print("Nezinau kiek tau")

# match veiksmas:
#     case '+':
#         a+b
#     case '-':
#         a-b