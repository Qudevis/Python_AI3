# Labas mano vardas Justas cia as aprasinesiu programini koda ir mokysiu Python 
# Cia kodas kurio dar gali prireikti
# Ctrl + / uzkomentuoja/atkomentuoja

# """Labas
# Mano vardas
# Yra Justas"""
# print(19)

# Print atspausdina teksta i terminala
# print((20))
# print(15)
# print((20))
# print(15)
# print((20))
# print(15)
# print((20))
# print(15)
# print((20))
# print(15)

# jono_amzius = 25
# antano_amzius = 30

# # print(jono_amzius)
# # print(jono_amzius)
# # print(jono_amzius)
# # print(jono_amzius)
# # print(jono_amzius)
# # print(antano_amzius)

# # jono_amzius_po_7_metu = jono_amzius + 7 # (25 + 7) # jono_amzius_po_7_metu = 32
# # print(jono_amzius_po_7_metu)

# kiek_antanas_vyresnis_uz_jona = antano_amzius - jono_amzius

# print(kiek_antanas_vyresnis_uz_jona)

# daugyba = antano_amzius * jono_amzius + 5 - 4 / 2

# print(daugyba - 3 * 5 / 16)

# vidurkis = 8.97 + 5 - 4.51

# print(vidurkis)

# print(7 % 3) # 7/3 ... 6/ 3 = 2.... Liekana 1 saldainis

# print(7 // 3) # 7/3 ... 6/ 3 = 2.... Liekana 1 saldainis

# skaicius % 2 jeigu liekana 0 tada lyginis skaicius jeigu liekana 1 tada nelyginis

# Skaicius = 15
# Mano_SKaicius = 15
# manoSkaicius = 15
# ManoSkaicius = 15
# mano_skaicius = 15

# _skaicius5 negali kintamieji prasideti skaiciumi arba simboliu

# amzius = 19
# Amzius = 20
# print(amzius)

# print = 19

# print(20) # 19(20)

# skaicius = 15

# skaicius = skaicius + 5
# skaicius /= 5

# print(skaicius)

# skaicius1 = 9
# skaicius2 = 7
# skaicius3 = 8.5
# skaicius4 = 5
# skaicius5 = 7.3

# suma = skaicius1 + skaicius2 + skaicius3 + skaicius4 + skaicius5

# vidurkis = suma / 5
# print(vidurkis)
# Justas = "Kazkas"
# Vardas = "Justas"

# Pavarde = "Kvederis"
# klaustukas = "?"
# pilnas_vardas = Vardas + " " + Pavarde + klaustukas

# print(pilnas_vardas)
# tekstas = "5" * 5
# print(tekstas)

# tekstas = "Labai \t\t geras tekstas kuris jums\\n parodys įdomų dalyką.\n O čia yra kitas sakinys,\n kuris taip pat reikalingas"
# print(tekstas)

# tekstas = "Čia yra mano tekstas, kuris man patinka ir aš labai stengiausi jį parašyti"

# print(tekstas[15]) # Paima 15 raide (skaiciuojant nuo nulio)
# print(tekstas[-2]) # paima antra nuo galo raide

# simbolis = tekstas[-2] # simbolis = "t"
# print(simbolis)

# print(tekstas[0:7]) # atspausdina visus simbolius nuo 0-tos pozicijos iki septintos (pirmas skaicius imtinai antras ne imtinai)

# print(tekstas[15:]) # nebutina uzpildyti visu skaiciu, jeigu neuzpildysime paims pirma arba paskutine reiksme ir istatys
# print(tekstas[-10:-15]) # Supraskime pirmas skaicius eina nuo, antras iki, negalime ju keisti vietomis
# print(tekstas[-10:]) # vienintelis validus variantas
# pirma_seka = tekstas[5:9]
# antra_seka = tekstas[9:15]
# pilna_seka = pirma_seka + antra_seka

# print(tekstas[0:51:2]) # 0 - pradzia 51 - pabaiga 2 - kas koki zingsni
# print(tekstas[::-1]) # -1 apsuka teksta


# text = "This text is an example of a string value"

# print(text)

# uppercase_text = text.upper() # nereikia cia skliausteliuose nieko, nes jis zino, kad dirbsime su tekstu

# print(uppercase_text)
# print(text.count("is")) # iesko kiek kartu pasikartoja nurodytas tekstas pilname tekste

# replaced = text.replace("is","hi")
# # print(text.replace("is","hi"))
# print(replaced)

# text = "Geras tekstas"
# text2 = "Dar geresnis tekstas"
# jonas_age = 20
# antanas_age = 30

# print("Jonui yra " + jonas_age + " metu")

# print(f"Jonui yra {jonas_age} metu, o Antanui yra {antanas_age} metu, o tekstas yra {text}") # f raidele igalina rasyti {} o juose kintamuosius

# # stringo viduje galima atlikti operacijas jeigu turime f raidele ir galima atlikti riestiniuose skliaustuose
# kintamasis = f"{jonas_age}, o antanui {antanas_age}, o jiem bendrai {jonas_age+antanas_age}" 

# print(kintamasis)

# kint = f"Mano tekstas yra {text.upper()}"
# print(kint)

# jonas_age_text = "20"
# antanas_age_text = "30"

# jonas_age = int(jonas_age_text)

# print(f"Bendrai jiems: {float(jonas_age_text)+int(antanas_age_text)} metu") # tipas() pvz int() konvertuoja i ta tipa


# print(f"Bendrai jiems: {jonas_age_text+antanas_age_text} metu") # bet jis konvertuoja tik tam kartui


# print("Jonui yra: " + str(jonas_age) + " metu")

# text = "Sitas tekstas yra geras tekstas"

# grazinta_kopija = text.replace("tekstas", "justas")
# print(text.replace("tekstas", "justas")) # text.replace("tekstas", "justas") -> Sitas justas yra geras justas -> print(Sitas justas yra geras justas)
# print(grazinta_kopija)

# vardas = input("Iveskite savo varda: ") # print("Iveskite savo varda: ") -> Laukiam ivesties (programa sustojus) -> vardas = ivestis (ivestis = "justas")
# pavarde = input("Iveskite savo pavarde: ")
# print(f"Sveiki, {vardas} {pavarde}")

# kiek metu man bus po 5 metu
# age = int(input("Iveskite savo amziu: ")) # -> "19" -> int("19")

# print(f"Jums bus {age+5} metu")