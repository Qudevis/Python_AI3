try:
    pass
# sarasas = [7,89,4,2,5,80]

# for el in sarasas: # 1 - iteracija el = sarasas[0], 2 iteracija el = sarasas[1]... per visus saraso elementus
#     # print(el)
#     test = 5 # sicia yra paskutinis sio kintamojo panaudojimas ar ne panaikins sita kintamaji ir nebeuzims vietos
#     continue
#     if 4 < 5:
#         pass
#     print(el)
#     print(el)

# # print(test)

# skaicius1, skaicius2, skaicius3 = 7, 9, 2

# print(skaicius2)

# sarasas = [7,89,4,2,5,80]

# # vieta = 0
# for vieta, skaicius in enumerate(sarasas): # sarasas[0] -> (0,7) -> skaicius, vieta = 0,7
#     # print(skaicius)
#     print(f"{skaicius} yra {vieta} vietoje")
#     # vieta += 1

# amziai = {"Jonas":15,"Antanas":25,"Mikas":30}

# for vardas in amziai.keys(): # is viso zodyno susidaro sarasas ["Jonas","antanas","Mikas"]
#     print(vardas)

# for metai in amziai.values(): # is viso zodyno susidaro sarasas [15,25,30]
#     print(metai)

# for vardas, metai in amziai.items(): # vardas, metai = Jonas, 15
#     print(f"{vardas} yra {metai} metu")


# [4,9,7,7] - sarasas

# {"Jonas":15} - zodynas

# (4,9,7,7) - tuple

# tuplas = (4,9,8, "Labas")
# print(tuplas)

# print(tuplas[0])
# print(type(tuplas))

# if not ("Justas" == "Jurgis"):
#     print("Tai ne tas pats vardas") 


# if "Justas" == "Jurgis":
#     pass
# else:
#     print("Tai ne tas pats vardas") 
except ValueError:
    print("Netinkamos reiksmes klaida")
    # irasyti i faila (log) kad tokiu ir tokiu laiku ivyko klaida tokia ir tokia
    # Isiusti el laiska administratoriui, kad ivyko kritine klaida ir tegul greiciau tvarko. 
except:
    print("Ivyko klaida")